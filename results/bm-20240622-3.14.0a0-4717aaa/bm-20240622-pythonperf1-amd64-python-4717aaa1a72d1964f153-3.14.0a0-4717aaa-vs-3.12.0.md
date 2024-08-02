# Results vs. 3.12.0

- fork: python
- ref: 4717aaa1a72d1964f153
- machine: windows-amd64
- commit hash: 4717aaa
- commit date: 2024-06-22
- overall geometric mean: 1.09x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240622-pythonperf1-amd64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 211 ms: 1.03x faster                                                       |
| docutils       | 1.66 sec                                                    | 1.62 sec: 1.03x faster                                                     |
| tornado_http   | 89.5 ms                                                     | 79.7 ms: 1.12x faster                                                      |
| Geometric mean | (ref)                                                       | 1.06x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240622-pythonperf1-amd64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none_tg         | 285 ms                                                      | 179 ms: 1.59x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 234 ms: 1.56x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 505 ms: 1.53x faster                                                       |
| async_tree_none            | 291 ms                                                      | 199 ms: 1.47x faster                                                       |
| async_tree_io              | 731 ms                                                      | 503 ms: 1.45x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 243 ms: 1.40x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 380 ms: 1.32x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 380 ms: 1.29x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.45x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240622-pythonperf1-amd64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 49.1 ms: 1.16x faster                                                      |
| nbody          | 71.9 ms                                                     | 65.8 ms: 1.09x faster                                                      |
| pidigits       | 152 ms                                                      | 149 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                       | 1.09x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240622-pythonperf1-amd64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 77.2 ms: 1.13x faster                                                      |
| regex_dna      | 126 ms                                                      | 124 ms: 1.02x faster                                                       |
| regex_v8       | 14.2 ms                                                     | 17.0 ms: 1.20x slower                                                      |
| Geometric mean | (ref)                                                       | 1.01x slower                                                               |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240622-pythonperf1-amd64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle_pure_python   | 195 us                                                      | 181 us: 1.08x faster                                                       |
| unpickle_pure_python | 133 us                                                      | 125 us: 1.07x faster                                                       |
| pickle               | 7.43 us                                                     | 7.10 us: 1.05x faster                                                      |
| xml_etree_generate   | 55.8 ms                                                     | 53.8 ms: 1.04x faster                                                      |
| xml_etree_iterparse  | 65.2 ms                                                     | 63.2 ms: 1.03x faster                                                      |
| xml_etree_process    | 37.7 ms                                                     | 36.9 ms: 1.02x faster                                                      |
| pickle_dict          | 18.4 us                                                     | 18.2 us: 1.01x faster                                                      |
| xml_etree_parse      | 93.0 ms                                                     | 92.0 ms: 1.01x faster                                                      |
| json_loads           | 13.9 us                                                     | 13.8 us: 1.01x faster                                                      |
| json_dumps           | 5.70 ms                                                     | 5.82 ms: 1.02x slower                                                      |
| unpickle_list        | 2.75 us                                                     | 2.84 us: 1.03x slower                                                      |
| pickle_list          | 2.83 us                                                     | 2.92 us: 1.03x slower                                                      |
| unpickle             | 8.18 us                                                     | 8.59 us: 1.05x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.01x faster                                                               |

Benchmark hidden because not significant (1): tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240622-pythonperf1-amd64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 16.8 ms: 1.03x slower                                                      |
| python_startup         | 19.5 ms                                                     | 20.7 ms: 1.06x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.05x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240622-pythonperf1-amd64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.60 ms: 1.07x faster                                                      |
| django_template | 22.9 ms                                                     | 22.1 ms: 1.04x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.06x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240622-pythonperf1-amd64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none_tg         | 285 ms                                                      | 179 ms: 1.59x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 234 ms: 1.56x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 505 ms: 1.53x faster                                                       |
| async_tree_none            | 291 ms                                                      | 199 ms: 1.47x faster                                                       |
| async_tree_io              | 731 ms                                                      | 503 ms: 1.45x faster                                                       |
| deepcopy                   | 238 us                                                      | 164 us: 1.45x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 243 ms: 1.40x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 17.1 us: 1.39x faster                                                      |
| comprehensions             | 14.1 us                                                     | 10.2 us: 1.39x faster                                                      |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.57 sec: 1.33x faster                                                     |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 380 ms: 1.32x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 380 ms: 1.29x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 1.68 us: 1.24x faster                                                      |
| raytrace                   | 192 ms                                                      | 159 ms: 1.21x faster                                                       |
| float                      | 56.8 ms                                                     | 49.1 ms: 1.16x faster                                                      |
| bench_thread_pool          | 857 us                                                      | 742 us: 1.15x faster                                                       |
| deltablue                  | 2.16 ms                                                     | 1.90 ms: 1.13x faster                                                      |
| chaos                      | 43.3 ms                                                     | 38.2 ms: 1.13x faster                                                      |
| regex_compile              | 87.5 ms                                                     | 77.2 ms: 1.13x faster                                                      |
| logging_silent             | 60.5 ns                                                     | 53.6 ns: 1.13x faster                                                      |
| nqueens                    | 62.8 ms                                                     | 55.8 ms: 1.12x faster                                                      |
| tornado_http               | 89.5 ms                                                     | 79.7 ms: 1.12x faster                                                      |
| hexiom                     | 4.10 ms                                                     | 3.70 ms: 1.11x faster                                                      |
| coroutines                 | 14.3 ms                                                     | 12.9 ms: 1.10x faster                                                      |
| scimark_lu                 | 58.9 ms                                                     | 53.4 ms: 1.10x faster                                                      |
| go                         | 91.6 ms                                                     | 83.6 ms: 1.10x faster                                                      |
| generators                 | 22.5 ms                                                     | 20.6 ms: 1.10x faster                                                      |
| richards                   | 28.4 ms                                                     | 25.9 ms: 1.10x faster                                                      |
| spectral_norm              | 66.9 ms                                                     | 61.2 ms: 1.09x faster                                                      |
| nbody                      | 71.9 ms                                                     | 65.8 ms: 1.09x faster                                                      |
| sqlite_synth               | 1.76 us                                                     | 1.61 us: 1.09x faster                                                      |
| richards_super             | 32.1 ms                                                     | 29.4 ms: 1.09x faster                                                      |
| logging_simple             | 6.28 us                                                     | 5.78 us: 1.09x faster                                                      |
| sympy_sum                  | 91.5 ms                                                     | 84.3 ms: 1.08x faster                                                      |
| sympy_str                  | 175 ms                                                      | 162 ms: 1.08x faster                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 40.5 ms: 1.08x faster                                                      |
| logging_format             | 6.72 us                                                     | 6.22 us: 1.08x faster                                                      |
| pickle_pure_python         | 195 us                                                      | 181 us: 1.08x faster                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 45.1 ms: 1.08x faster                                                      |
| mako                       | 7.09 ms                                                     | 6.60 ms: 1.07x faster                                                      |
| unpickle_pure_python       | 133 us                                                      | 125 us: 1.07x faster                                                       |
| pprint_safe_repr           | 513 ms                                                      | 481 ms: 1.07x faster                                                       |
| pathlib                    | 80.5 ms                                                     | 75.5 ms: 1.07x faster                                                      |
| scimark_fft                | 184 ms                                                      | 173 ms: 1.06x faster                                                       |
| sqlglot_normalize          | 187 ms                                                      | 176 ms: 1.06x faster                                                       |
| pprint_pformat             | 1.05 sec                                                    | 986 ms: 1.06x faster                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 65.3 ms: 1.06x faster                                                      |
| sqlglot_transpile          | 1.02 ms                                                     | 966 us: 1.06x faster                                                       |
| json                       | 3.05 ms                                                     | 2.88 ms: 1.06x faster                                                      |
| meteor_contest             | 74.6 ms                                                     | 70.6 ms: 1.06x faster                                                      |
| sympy_integrate            | 13.0 ms                                                     | 12.3 ms: 1.05x faster                                                      |
| pyflate                    | 295 ms                                                      | 281 ms: 1.05x faster                                                       |
| async_generators           | 239 ms                                                      | 228 ms: 1.05x faster                                                       |
| pickle                     | 7.43 us                                                     | 7.10 us: 1.05x faster                                                      |
| scimark_sor                | 78.8 ms                                                     | 75.4 ms: 1.04x faster                                                      |
| sqlglot_parse              | 804 us                                                      | 771 us: 1.04x faster                                                       |
| sqlglot_optimize           | 34.5 ms                                                     | 33.1 ms: 1.04x faster                                                      |
| django_template            | 22.9 ms                                                     | 22.1 ms: 1.04x faster                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 53.8 ms: 1.04x faster                                                      |
| 2to3                       | 218 ms                                                      | 211 ms: 1.03x faster                                                       |
| sympy_expand               | 284 ms                                                      | 275 ms: 1.03x faster                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 63.2 ms: 1.03x faster                                                      |
| asyncio_tcp                | 487 ms                                                      | 473 ms: 1.03x faster                                                       |
| docutils                   | 1.66 sec                                                    | 1.62 sec: 1.03x faster                                                     |
| xml_etree_process          | 37.7 ms                                                     | 36.9 ms: 1.02x faster                                                      |
| pidigits                   | 152 ms                                                      | 149 ms: 1.02x faster                                                       |
| regex_dna                  | 126 ms                                                      | 124 ms: 1.02x faster                                                       |
| pickle_dict                | 18.4 us                                                     | 18.2 us: 1.01x faster                                                      |
| xml_etree_parse            | 93.0 ms                                                     | 92.0 ms: 1.01x faster                                                      |
| fannkuch                   | 247 ms                                                      | 245 ms: 1.01x faster                                                       |
| json_loads                 | 13.9 us                                                     | 13.8 us: 1.01x faster                                                      |
| mdp                        | 1.37 sec                                                    | 1.38 sec: 1.01x slower                                                     |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.59 ms: 1.01x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 1.56 ms: 1.02x slower                                                      |
| json_dumps                 | 5.70 ms                                                     | 5.82 ms: 1.02x slower                                                      |
| unpickle_list              | 2.75 us                                                     | 2.84 us: 1.03x slower                                                      |
| pickle_list                | 2.83 us                                                     | 2.92 us: 1.03x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 16.8 ms: 1.03x slower                                                      |
| unpickle                   | 8.18 us                                                     | 8.59 us: 1.05x slower                                                      |
| python_startup             | 19.5 ms                                                     | 20.7 ms: 1.06x slower                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 102 us: 1.08x slower                                                       |
| coverage                   | 40.8 ms                                                     | 46.8 ms: 1.15x slower                                                      |
| telco                      | 4.13 ms                                                     | 4.93 ms: 1.19x slower                                                      |
| regex_v8                   | 14.2 ms                                                     | 17.0 ms: 1.20x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 914 us: 1.21x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.09x faster                                                               |

Benchmark hidden because not significant (3): tomli_loads, regex_effbot, pycparser
Ignored benchmarks (8) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (5) of results/bm-20240622-3.14.0a0-4717aaa/bm-20240622-pythonperf1-amd64-python-4717aaa1a72d1964f153-3.14.0a0-4717aaa.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: unknown