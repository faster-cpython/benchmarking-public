# Results vs. 3.12.0

- fork: python
- ref: b3aa1b5fe260382788a2
- machine: windows-amd64
- commit hash: b3aa1b5
- commit date: 2024-10-11
- overall geometric mean: 1.01x slower
- HPT reliability: 99.84%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241011-pythonperf1-amd64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 229 ms: 1.05x slower                                                       |
| docutils       | 1.66 sec                                                    | 1.72 sec: 1.04x slower                                                     |
| tornado_http   | 89.5 ms                                                     | 94.9 ms: 1.06x slower                                                      |
| Geometric mean | (ref)                                                       | 1.05x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241011-pythonperf1-amd64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 258 ms: 1.42x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 207 ms: 1.38x faster                                                       |
| async_tree_none            | 291 ms                                                      | 214 ms: 1.36x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 579 ms: 1.33x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 391 ms: 1.29x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 272 ms: 1.25x faster                                                       |
| async_tree_io              | 731 ms                                                      | 591 ms: 1.24x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 396 ms: 1.24x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.31x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241011-pythonperf1-amd64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 53.8 ms: 1.06x faster                                                      |
| pidigits       | 152 ms                                                      | 149 ms: 1.02x faster                                                       |
| nbody          | 71.9 ms                                                     | 79.3 ms: 1.10x slower                                                      |
| Geometric mean | (ref)                                                       | 1.01x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241011-pythonperf1-amd64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 120 ms: 1.05x faster                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.57 ms: 1.03x faster                                                      |
| regex_compile  | 87.5 ms                                                     | 91.3 ms: 1.04x slower                                                      |
| regex_v8       | 14.2 ms                                                     | 15.3 ms: 1.08x slower                                                      |
| Geometric mean | (ref)                                                       | 1.01x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241011-pythonperf1-amd64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle               | 7.43 us                                                     | 7.25 us: 1.03x faster                                                      |
| xml_etree_iterparse  | 65.2 ms                                                     | 66.3 ms: 1.02x slower                                                      |
| unpickle_list        | 2.75 us                                                     | 2.80 us: 1.02x slower                                                      |
| xml_etree_generate   | 55.8 ms                                                     | 57.4 ms: 1.03x slower                                                      |
| xml_etree_parse      | 93.0 ms                                                     | 96.5 ms: 1.04x slower                                                      |
| pickle_dict          | 18.4 us                                                     | 19.2 us: 1.04x slower                                                      |
| pickle_list          | 2.83 us                                                     | 2.95 us: 1.04x slower                                                      |
| json_loads           | 13.9 us                                                     | 14.7 us: 1.06x slower                                                      |
| xml_etree_process    | 37.7 ms                                                     | 40.2 ms: 1.06x slower                                                      |
| unpickle_pure_python | 133 us                                                      | 148 us: 1.11x slower                                                       |
| pickle_pure_python   | 195 us                                                      | 220 us: 1.13x slower                                                       |
| unpickle             | 8.18 us                                                     | 9.40 us: 1.15x slower                                                      |
| json_dumps           | 5.70 ms                                                     | 6.75 ms: 1.18x slower                                                      |
| tomli_loads          | 1.37 sec                                                    | 1.64 sec: 1.20x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.07x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241011-pythonperf1-amd64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 18.2 ms: 1.12x slower                                                      |
| python_startup         | 19.5 ms                                                     | 22.3 ms: 1.14x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.13x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241011-pythonperf1-amd64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.78 ms: 1.05x faster                                                      |
| django_template | 22.9 ms                                                     | 25.7 ms: 1.12x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.04x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241011-pythonperf1-amd64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 258 ms: 1.42x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 207 ms: 1.38x faster                                                       |
| async_tree_none            | 291 ms                                                      | 214 ms: 1.36x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 579 ms: 1.33x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 391 ms: 1.29x faster                                                       |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.65 sec: 1.27x faster                                                     |
| async_tree_memoization     | 339 ms                                                      | 272 ms: 1.25x faster                                                       |
| async_tree_io              | 731 ms                                                      | 591 ms: 1.24x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 396 ms: 1.24x faster                                                       |
| deepcopy                   | 238 us                                                      | 193 us: 1.23x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 19.7 us: 1.20x faster                                                      |
| comprehensions             | 14.1 us                                                     | 11.8 us: 1.20x faster                                                      |
| go                         | 91.6 ms                                                     | 86.4 ms: 1.06x faster                                                      |
| sqlite_synth               | 1.76 us                                                     | 1.67 us: 1.06x faster                                                      |
| float                      | 56.8 ms                                                     | 53.8 ms: 1.06x faster                                                      |
| bench_thread_pool          | 857 us                                                      | 812 us: 1.06x faster                                                       |
| regex_dna                  | 126 ms                                                      | 120 ms: 1.05x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 2.00 us: 1.05x faster                                                      |
| generators                 | 22.5 ms                                                     | 21.5 ms: 1.05x faster                                                      |
| mako                       | 7.09 ms                                                     | 6.78 ms: 1.05x faster                                                      |
| unpack_sequence            | 37.5 ns                                                     | 36.0 ns: 1.04x faster                                                      |
| coroutines                 | 14.3 ms                                                     | 13.8 ms: 1.03x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.57 ms: 1.03x faster                                                      |
| pickle                     | 7.43 us                                                     | 7.25 us: 1.03x faster                                                      |
| pidigits                   | 152 ms                                                      | 149 ms: 1.02x faster                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 48.1 ms: 1.01x faster                                                      |
| scimark_lu                 | 58.9 ms                                                     | 58.4 ms: 1.01x faster                                                      |
| sympy_sum                  | 91.5 ms                                                     | 90.9 ms: 1.01x faster                                                      |
| dulwich_log                | 44.3 ms                                                     | 44.5 ms: 1.01x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 1.53 ms: 1.01x slower                                                      |
| chaos                      | 43.3 ms                                                     | 43.7 ms: 1.01x slower                                                      |
| logging_simple             | 6.28 us                                                     | 6.38 us: 1.02x slower                                                      |
| xml_etree_iterparse        | 65.2 ms                                                     | 66.3 ms: 1.02x slower                                                      |
| unpickle_list              | 2.75 us                                                     | 2.80 us: 1.02x slower                                                      |
| sympy_str                  | 175 ms                                                      | 178 ms: 1.02x slower                                                       |
| logging_format             | 6.72 us                                                     | 6.85 us: 1.02x slower                                                      |
| spectral_norm              | 66.9 ms                                                     | 68.3 ms: 1.02x slower                                                      |
| nqueens                    | 62.8 ms                                                     | 64.4 ms: 1.03x slower                                                      |
| meteor_contest             | 74.6 ms                                                     | 76.6 ms: 1.03x slower                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 57.4 ms: 1.03x slower                                                      |
| xml_etree_parse            | 93.0 ms                                                     | 96.5 ms: 1.04x slower                                                      |
| docutils                   | 1.66 sec                                                    | 1.72 sec: 1.04x slower                                                     |
| async_generators           | 239 ms                                                      | 249 ms: 1.04x slower                                                       |
| sympy_integrate            | 13.0 ms                                                     | 13.5 ms: 1.04x slower                                                      |
| regex_compile              | 87.5 ms                                                     | 91.3 ms: 1.04x slower                                                      |
| pickle_dict                | 18.4 us                                                     | 19.2 us: 1.04x slower                                                      |
| pickle_list                | 2.83 us                                                     | 2.95 us: 1.04x slower                                                      |
| deltablue                  | 2.16 ms                                                     | 2.26 ms: 1.05x slower                                                      |
| sqlglot_normalize          | 187 ms                                                      | 196 ms: 1.05x slower                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.68 ms: 1.05x slower                                                      |
| 2to3                       | 218 ms                                                      | 229 ms: 1.05x slower                                                       |
| hexiom                     | 4.10 ms                                                     | 4.33 ms: 1.06x slower                                                      |
| json_loads                 | 13.9 us                                                     | 14.7 us: 1.06x slower                                                      |
| tornado_http               | 89.5 ms                                                     | 94.9 ms: 1.06x slower                                                      |
| pycparser                  | 699 ms                                                      | 743 ms: 1.06x slower                                                       |
| xml_etree_process          | 37.7 ms                                                     | 40.2 ms: 1.06x slower                                                      |
| pprint_safe_repr           | 513 ms                                                      | 547 ms: 1.07x slower                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 46.7 ms: 1.07x slower                                                      |
| sqlglot_optimize           | 34.5 ms                                                     | 36.9 ms: 1.07x slower                                                      |
| pprint_pformat             | 1.05 sec                                                    | 1.12 sec: 1.07x slower                                                     |
| raytrace                   | 192 ms                                                      | 207 ms: 1.08x slower                                                       |
| regex_v8                   | 14.2 ms                                                     | 15.3 ms: 1.08x slower                                                      |
| pyflate                    | 295 ms                                                      | 318 ms: 1.08x slower                                                       |
| sympy_expand               | 284 ms                                                      | 309 ms: 1.09x slower                                                       |
| scimark_fft                | 184 ms                                                      | 203 ms: 1.10x slower                                                       |
| nbody                      | 71.9 ms                                                     | 79.3 ms: 1.10x slower                                                      |
| sqlglot_transpile          | 1.02 ms                                                     | 1.14 ms: 1.11x slower                                                      |
| unpickle_pure_python       | 133 us                                                      | 148 us: 1.11x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 18.2 ms: 1.12x slower                                                      |
| scimark_sor                | 78.8 ms                                                     | 88.2 ms: 1.12x slower                                                      |
| django_template            | 22.9 ms                                                     | 25.7 ms: 1.12x slower                                                      |
| pickle_pure_python         | 195 us                                                      | 220 us: 1.13x slower                                                       |
| sqlglot_parse              | 804 us                                                      | 908 us: 1.13x slower                                                       |
| richards_super             | 32.1 ms                                                     | 36.2 ms: 1.13x slower                                                      |
| richards                   | 28.4 ms                                                     | 32.1 ms: 1.13x slower                                                      |
| mdp                        | 1.37 sec                                                    | 1.55 sec: 1.13x slower                                                     |
| coverage                   | 40.8 ms                                                     | 46.6 ms: 1.14x slower                                                      |
| fannkuch                   | 247 ms                                                      | 282 ms: 1.14x slower                                                       |
| python_startup             | 19.5 ms                                                     | 22.3 ms: 1.14x slower                                                      |
| unpickle                   | 8.18 us                                                     | 9.40 us: 1.15x slower                                                      |
| asyncio_tcp                | 487 ms                                                      | 568 ms: 1.17x slower                                                       |
| telco                      | 4.13 ms                                                     | 4.83 ms: 1.17x slower                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 112 us: 1.17x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 6.75 ms: 1.18x slower                                                      |
| tomli_loads                | 1.37 sec                                                    | 1.64 sec: 1.20x slower                                                     |
| create_gc_cycles           | 752 us                                                      | 923 us: 1.23x slower                                                       |
| json                       | 3.05 ms                                                     | 4.18 ms: 1.37x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.01x slower                                                               |

Benchmark hidden because not significant (3): pathlib, bench_mp_pool, logging_silent
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20241011-3.14.0a0-b3aa1b5/bm-20241011-pythonperf1-amd64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.84% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown