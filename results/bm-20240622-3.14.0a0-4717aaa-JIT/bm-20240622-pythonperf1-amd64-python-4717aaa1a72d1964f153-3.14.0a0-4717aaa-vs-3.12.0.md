# Results vs. 3.12.0

- fork: python
- ref: 4717aaa1a72d1964f153
- machine: windows-amd64
- commit hash: 4717aaa
- commit date: 2024-06-22
- overall geometric mean: 1.09x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.01x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240622-pythonperf1-amd64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 228 ms: 1.05x slower                                                       |
| docutils       | 1.66 sec                                                    | 1.74 sec: 1.05x slower                                                     |
| tornado_http   | 89.5 ms                                                     | 82.7 ms: 1.08x faster                                                      |
| Geometric mean | (ref)                                                       | 1.00x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240622-pythonperf1-amd64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none_tg         | 285 ms                                                      | 178 ms: 1.60x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 234 ms: 1.57x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 505 ms: 1.53x faster                                                       |
| async_tree_io              | 731 ms                                                      | 495 ms: 1.48x faster                                                       |
| async_tree_none            | 291 ms                                                      | 198 ms: 1.47x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 242 ms: 1.40x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 372 ms: 1.35x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 377 ms: 1.30x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.46x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240622-pythonperf1-amd64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 53.6 ms: 1.34x faster                                                      |
| float          | 56.8 ms                                                     | 44.0 ms: 1.29x faster                                                      |
| pidigits       | 152 ms                                                      | 149 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                       | 1.21x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240622-pythonperf1-amd64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 118 ms: 1.08x faster                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.56 ms: 1.03x faster                                                      |
| regex_v8       | 14.2 ms                                                     | 17.2 ms: 1.21x slower                                                      |
| Geometric mean | (ref)                                                       | 1.02x slower                                                               |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240622-pythonperf1-amd64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle_pure_python   | 195 us                                                      | 168 us: 1.16x faster                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.21 sec: 1.13x faster                                                     |
| xml_etree_generate   | 55.8 ms                                                     | 51.3 ms: 1.09x faster                                                      |
| unpickle_pure_python | 133 us                                                      | 123 us: 1.08x faster                                                       |
| xml_etree_iterparse  | 65.2 ms                                                     | 60.9 ms: 1.07x faster                                                      |
| xml_etree_process    | 37.7 ms                                                     | 36.2 ms: 1.04x faster                                                      |
| pickle_dict          | 18.4 us                                                     | 17.7 us: 1.04x faster                                                      |
| pickle               | 7.43 us                                                     | 7.29 us: 1.02x faster                                                      |
| json_dumps           | 5.70 ms                                                     | 5.65 ms: 1.01x faster                                                      |
| json_loads           | 13.9 us                                                     | 14.0 us: 1.01x slower                                                      |
| pickle_list          | 2.83 us                                                     | 2.86 us: 1.01x slower                                                      |
| unpickle_list        | 2.75 us                                                     | 2.80 us: 1.02x slower                                                      |
| unpickle             | 8.18 us                                                     | 9.00 us: 1.10x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.04x faster                                                               |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240622-pythonperf1-amd64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 18.4 ms: 1.13x slower                                                      |
| python_startup         | 19.5 ms                                                     | 22.5 ms: 1.16x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.14x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240622-pythonperf1-amd64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.08 ms: 1.40x faster                                                      |
| django_template | 22.9 ms                                                     | 24.6 ms: 1.07x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.14x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240622-pythonperf1-amd64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none_tg         | 285 ms                                                      | 178 ms: 1.60x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 234 ms: 1.57x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 15.3 us: 1.55x faster                                                      |
| async_tree_io_tg           | 771 ms                                                      | 505 ms: 1.53x faster                                                       |
| async_tree_io              | 731 ms                                                      | 495 ms: 1.48x faster                                                       |
| async_tree_none            | 291 ms                                                      | 198 ms: 1.47x faster                                                       |
| spectral_norm              | 66.9 ms                                                     | 46.3 ms: 1.45x faster                                                      |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.48 sec: 1.42x faster                                                     |
| async_tree_memoization     | 339 ms                                                      | 242 ms: 1.40x faster                                                       |
| mako                       | 7.09 ms                                                     | 5.08 ms: 1.40x faster                                                      |
| comprehensions             | 14.1 us                                                     | 10.2 us: 1.38x faster                                                      |
| deepcopy                   | 238 us                                                      | 175 us: 1.36x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 372 ms: 1.35x faster                                                       |
| nbody                      | 71.9 ms                                                     | 53.6 ms: 1.34x faster                                                      |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 377 ms: 1.30x faster                                                       |
| float                      | 56.8 ms                                                     | 44.0 ms: 1.29x faster                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 1.68 us: 1.25x faster                                                      |
| scimark_fft                | 184 ms                                                      | 150 ms: 1.23x faster                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.09 ms: 1.22x faster                                                      |
| crypto_pyaes               | 48.5 ms                                                     | 40.7 ms: 1.19x faster                                                      |
| scimark_monte_carlo        | 43.7 ms                                                     | 37.4 ms: 1.17x faster                                                      |
| pyflate                    | 295 ms                                                      | 252 ms: 1.17x faster                                                       |
| pickle_pure_python         | 195 us                                                      | 168 us: 1.16x faster                                                       |
| raytrace                   | 192 ms                                                      | 168 ms: 1.15x faster                                                       |
| logging_simple             | 6.28 us                                                     | 5.49 us: 1.14x faster                                                      |
| logging_format             | 6.72 us                                                     | 5.87 us: 1.14x faster                                                      |
| pprint_safe_repr           | 513 ms                                                      | 450 ms: 1.14x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.21 sec: 1.13x faster                                                     |
| pprint_pformat             | 1.05 sec                                                    | 924 ms: 1.13x faster                                                       |
| chaos                      | 43.3 ms                                                     | 38.5 ms: 1.13x faster                                                      |
| generators                 | 22.5 ms                                                     | 20.0 ms: 1.12x faster                                                      |
| sqlite_synth               | 1.76 us                                                     | 1.58 us: 1.12x faster                                                      |
| bench_thread_pool          | 857 us                                                      | 768 us: 1.11x faster                                                       |
| fannkuch                   | 247 ms                                                      | 222 ms: 1.11x faster                                                       |
| coroutines                 | 14.3 ms                                                     | 12.8 ms: 1.11x faster                                                      |
| logging_silent             | 60.5 ns                                                     | 55.4 ns: 1.09x faster                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 51.3 ms: 1.09x faster                                                      |
| tornado_http               | 89.5 ms                                                     | 82.7 ms: 1.08x faster                                                      |
| unpickle_pure_python       | 133 us                                                      | 123 us: 1.08x faster                                                       |
| regex_dna                  | 126 ms                                                      | 118 ms: 1.08x faster                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 60.9 ms: 1.07x faster                                                      |
| pathlib                    | 80.5 ms                                                     | 75.7 ms: 1.06x faster                                                      |
| nqueens                    | 62.8 ms                                                     | 59.5 ms: 1.06x faster                                                      |
| xml_etree_process          | 37.7 ms                                                     | 36.2 ms: 1.04x faster                                                      |
| pickle_dict                | 18.4 us                                                     | 17.7 us: 1.04x faster                                                      |
| go                         | 91.6 ms                                                     | 88.0 ms: 1.04x faster                                                      |
| json                       | 3.05 ms                                                     | 2.93 ms: 1.04x faster                                                      |
| sqlglot_parse              | 804 us                                                      | 775 us: 1.04x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.56 ms: 1.03x faster                                                      |
| deltablue                  | 2.16 ms                                                     | 2.09 ms: 1.03x faster                                                      |
| meteor_contest             | 74.6 ms                                                     | 72.6 ms: 1.03x faster                                                      |
| pidigits                   | 152 ms                                                      | 149 ms: 1.02x faster                                                       |
| pickle                     | 7.43 us                                                     | 7.29 us: 1.02x faster                                                      |
| sqlglot_transpile          | 1.02 ms                                                     | 1.01 ms: 1.02x faster                                                      |
| sympy_sum                  | 91.5 ms                                                     | 90.5 ms: 1.01x faster                                                      |
| json_dumps                 | 5.70 ms                                                     | 5.65 ms: 1.01x faster                                                      |
| scimark_sor                | 78.8 ms                                                     | 79.3 ms: 1.01x slower                                                      |
| sqlglot_normalize          | 187 ms                                                      | 188 ms: 1.01x slower                                                       |
| json_loads                 | 13.9 us                                                     | 14.0 us: 1.01x slower                                                      |
| bench_mp_pool              | 69.2 ms                                                     | 69.9 ms: 1.01x slower                                                      |
| pickle_list                | 2.83 us                                                     | 2.86 us: 1.01x slower                                                      |
| async_generators           | 239 ms                                                      | 243 ms: 1.02x slower                                                       |
| unpickle_list              | 2.75 us                                                     | 2.80 us: 1.02x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 1.56 ms: 1.03x slower                                                      |
| sqlglot_optimize           | 34.5 ms                                                     | 35.6 ms: 1.03x slower                                                      |
| 2to3                       | 218 ms                                                      | 228 ms: 1.05x slower                                                       |
| docutils                   | 1.66 sec                                                    | 1.74 sec: 1.05x slower                                                     |
| sympy_integrate            | 13.0 ms                                                     | 13.6 ms: 1.05x slower                                                      |
| richards_super             | 32.1 ms                                                     | 33.8 ms: 1.05x slower                                                      |
| richards                   | 28.4 ms                                                     | 30.2 ms: 1.06x slower                                                      |
| coverage                   | 40.8 ms                                                     | 43.6 ms: 1.07x slower                                                      |
| django_template            | 22.9 ms                                                     | 24.6 ms: 1.07x slower                                                      |
| sympy_expand               | 284 ms                                                      | 305 ms: 1.08x slower                                                       |
| telco                      | 4.13 ms                                                     | 4.48 ms: 1.08x slower                                                      |
| unpickle                   | 8.18 us                                                     | 9.00 us: 1.10x slower                                                      |
| hexiom                     | 4.10 ms                                                     | 4.62 ms: 1.13x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 18.4 ms: 1.13x slower                                                      |
| pycparser                  | 699 ms                                                      | 796 ms: 1.14x slower                                                       |
| python_startup             | 19.5 ms                                                     | 22.5 ms: 1.16x slower                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 110 us: 1.16x slower                                                       |
| scimark_lu                 | 58.9 ms                                                     | 68.8 ms: 1.17x slower                                                      |
| regex_v8                   | 14.2 ms                                                     | 17.2 ms: 1.21x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 914 us: 1.21x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.09x faster                                                               |

Benchmark hidden because not significant (5): asyncio_tcp, xml_etree_parse, regex_compile, mdp, sympy_str
Ignored benchmarks (8) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (5) of results/bm-20240622-3.14.0a0-4717aaa-JIT/bm-20240622-pythonperf1-amd64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: unknown