# Results vs. 3.12.0

- fork: python
- ref: 68e279b37aae3019979a
- machine: windows-amd64
- commit hash: 68e279b
- commit date: 2024-07-07
- overall geometric mean: 1.07x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240707-pythonperf1-amd64-python-68e279b37aae3019979a-3.14.0a0-68e279b |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 214 ms: 1.02x faster                                                       |
| docutils       | 1.66 sec                                                    | 1.63 sec: 1.02x faster                                                     |
| tornado_http   | 89.5 ms                                                     | 80.9 ms: 1.11x faster                                                      |
| Geometric mean | (ref)                                                       | 1.05x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240707-pythonperf1-amd64-python-68e279b37aae3019979a-3.14.0a0-68e279b |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none_tg         | 285 ms                                                      | 186 ms: 1.54x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 241 ms: 1.52x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 516 ms: 1.49x faster                                                       |
| async_tree_none            | 291 ms                                                      | 205 ms: 1.42x faster                                                       |
| async_tree_io              | 731 ms                                                      | 522 ms: 1.40x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 250 ms: 1.36x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 382 ms: 1.31x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 380 ms: 1.29x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.41x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240707-pythonperf1-amd64-python-68e279b37aae3019979a-3.14.0a0-68e279b |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 52.6 ms: 1.08x faster                                                      |
| pidigits       | 152 ms                                                      | 150 ms: 1.01x faster                                                       |
| nbody          | 71.9 ms                                                     | 73.2 ms: 1.02x slower                                                      |
| Geometric mean | (ref)                                                       | 1.02x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240707-pythonperf1-amd64-python-68e279b37aae3019979a-3.14.0a0-68e279b |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 78.5 ms: 1.11x faster                                                      |
| regex_dna      | 126 ms                                                      | 122 ms: 1.04x faster                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.59 ms: 1.01x faster                                                      |
| regex_v8       | 14.2 ms                                                     | 17.1 ms: 1.20x slower                                                      |
| Geometric mean | (ref)                                                       | 1.01x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240707-pythonperf1-amd64-python-68e279b37aae3019979a-3.14.0a0-68e279b |
|---------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle_pure_python  | 195 us                                                      | 186 us: 1.05x faster                                                       |
| xml_etree_iterparse | 65.2 ms                                                     | 63.8 ms: 1.02x faster                                                      |
| xml_etree_generate  | 55.8 ms                                                     | 55.0 ms: 1.02x faster                                                      |
| xml_etree_parse     | 93.0 ms                                                     | 92.4 ms: 1.01x faster                                                      |
| json_dumps          | 5.70 ms                                                     | 5.66 ms: 1.01x faster                                                      |
| json_loads          | 13.9 us                                                     | 14.0 us: 1.01x slower                                                      |
| tomli_loads         | 1.37 sec                                                    | 1.47 sec: 1.07x slower                                                     |
| Geometric mean      | (ref)                                                       | 1.00x faster                                                               |

Benchmark hidden because not significant (2): unpickle_pure_python, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240707-pythonperf1-amd64-python-68e279b37aae3019979a-3.14.0a0-68e279b |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 16.7 ms: 1.03x slower                                                      |
| python_startup         | 19.5 ms                                                     | 20.9 ms: 1.07x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.05x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240707-pythonperf1-amd64-python-68e279b37aae3019979a-3.14.0a0-68e279b |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.59 ms: 1.08x faster                                                      |
| django_template | 22.9 ms                                                     | 23.2 ms: 1.01x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.03x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240707-pythonperf1-amd64-python-68e279b37aae3019979a-3.14.0a0-68e279b |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none_tg         | 285 ms                                                      | 186 ms: 1.54x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 241 ms: 1.52x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 516 ms: 1.49x faster                                                       |
| async_tree_none            | 291 ms                                                      | 205 ms: 1.42x faster                                                       |
| async_tree_io              | 731 ms                                                      | 522 ms: 1.40x faster                                                       |
| deepcopy                   | 238 us                                                      | 170 us: 1.40x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 250 ms: 1.36x faster                                                       |
| comprehensions             | 14.1 us                                                     | 10.6 us: 1.34x faster                                                      |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 382 ms: 1.31x faster                                                       |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.60 sec: 1.31x faster                                                     |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 380 ms: 1.29x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 18.6 us: 1.27x faster                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 1.76 us: 1.19x faster                                                      |
| raytrace                   | 192 ms                                                      | 167 ms: 1.15x faster                                                       |
| bench_thread_pool          | 857 us                                                      | 750 us: 1.14x faster                                                       |
| regex_compile              | 87.5 ms                                                     | 78.5 ms: 1.11x faster                                                      |
| tornado_http               | 89.5 ms                                                     | 80.9 ms: 1.11x faster                                                      |
| chaos                      | 43.3 ms                                                     | 39.2 ms: 1.11x faster                                                      |
| deltablue                  | 2.16 ms                                                     | 1.99 ms: 1.09x faster                                                      |
| float                      | 56.8 ms                                                     | 52.6 ms: 1.08x faster                                                      |
| nqueens                    | 62.8 ms                                                     | 58.2 ms: 1.08x faster                                                      |
| sympy_sum                  | 91.5 ms                                                     | 84.9 ms: 1.08x faster                                                      |
| mako                       | 7.09 ms                                                     | 6.59 ms: 1.08x faster                                                      |
| coroutines                 | 14.3 ms                                                     | 13.3 ms: 1.07x faster                                                      |
| spectral_norm              | 66.9 ms                                                     | 62.3 ms: 1.07x faster                                                      |
| generators                 | 22.5 ms                                                     | 21.0 ms: 1.07x faster                                                      |
| sympy_str                  | 175 ms                                                      | 164 ms: 1.07x faster                                                       |
| go                         | 91.6 ms                                                     | 85.7 ms: 1.07x faster                                                      |
| sqlglot_normalize          | 187 ms                                                      | 175 ms: 1.07x faster                                                       |
| logging_simple             | 6.28 us                                                     | 5.89 us: 1.07x faster                                                      |
| bench_mp_pool              | 69.2 ms                                                     | 65.0 ms: 1.06x faster                                                      |
| pathlib                    | 80.5 ms                                                     | 75.7 ms: 1.06x faster                                                      |
| logging_format             | 6.72 us                                                     | 6.33 us: 1.06x faster                                                      |
| richards                   | 28.4 ms                                                     | 26.9 ms: 1.05x faster                                                      |
| hexiom                     | 4.10 ms                                                     | 3.90 ms: 1.05x faster                                                      |
| pickle_pure_python         | 195 us                                                      | 186 us: 1.05x faster                                                       |
| richards_super             | 32.1 ms                                                     | 30.6 ms: 1.05x faster                                                      |
| logging_silent             | 60.5 ns                                                     | 57.9 ns: 1.04x faster                                                      |
| sqlglot_optimize           | 34.5 ms                                                     | 33.1 ms: 1.04x faster                                                      |
| json                       | 3.05 ms                                                     | 2.94 ms: 1.04x faster                                                      |
| regex_dna                  | 126 ms                                                      | 122 ms: 1.04x faster                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 46.8 ms: 1.04x faster                                                      |
| sympy_integrate            | 13.0 ms                                                     | 12.5 ms: 1.04x faster                                                      |
| pprint_pformat             | 1.05 sec                                                    | 1.01 sec: 1.03x faster                                                     |
| pprint_safe_repr           | 513 ms                                                      | 496 ms: 1.03x faster                                                       |
| async_generators           | 239 ms                                                      | 233 ms: 1.03x faster                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 63.8 ms: 1.02x faster                                                      |
| sympy_expand               | 284 ms                                                      | 278 ms: 1.02x faster                                                       |
| 2to3                       | 218 ms                                                      | 214 ms: 1.02x faster                                                       |
| docutils                   | 1.66 sec                                                    | 1.63 sec: 1.02x faster                                                     |
| xml_etree_generate         | 55.8 ms                                                     | 55.0 ms: 1.02x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.59 ms: 1.01x faster                                                      |
| pidigits                   | 152 ms                                                      | 150 ms: 1.01x faster                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 92.4 ms: 1.01x faster                                                      |
| pyflate                    | 295 ms                                                      | 293 ms: 1.01x faster                                                       |
| json_dumps                 | 5.70 ms                                                     | 5.66 ms: 1.01x faster                                                      |
| scimark_sor                | 78.8 ms                                                     | 78.4 ms: 1.00x faster                                                      |
| meteor_contest             | 74.6 ms                                                     | 74.9 ms: 1.00x slower                                                      |
| json_loads                 | 13.9 us                                                     | 14.0 us: 1.01x slower                                                      |
| django_template            | 22.9 ms                                                     | 23.2 ms: 1.01x slower                                                      |
| sqlglot_parse              | 804 us                                                      | 813 us: 1.01x slower                                                       |
| scimark_lu                 | 58.9 ms                                                     | 59.8 ms: 1.02x slower                                                      |
| nbody                      | 71.9 ms                                                     | 73.2 ms: 1.02x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 1.55 ms: 1.02x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 16.7 ms: 1.03x slower                                                      |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.64 ms: 1.03x slower                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 102 us: 1.07x slower                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.47 sec: 1.07x slower                                                     |
| python_startup             | 19.5 ms                                                     | 20.9 ms: 1.07x slower                                                      |
| mdp                        | 1.37 sec                                                    | 1.50 sec: 1.09x slower                                                     |
| fannkuch                   | 247 ms                                                      | 273 ms: 1.11x slower                                                       |
| coverage                   | 40.8 ms                                                     | 45.8 ms: 1.12x slower                                                      |
| telco                      | 4.13 ms                                                     | 4.69 ms: 1.14x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 885 us: 1.18x slower                                                       |
| regex_v8                   | 14.2 ms                                                     | 17.1 ms: 1.20x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.07x faster                                                               |

Benchmark hidden because not significant (7): asyncio_tcp, scimark_monte_carlo, unpickle_pure_python, scimark_fft, xml_etree_process, sqlglot_transpile, pycparser
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240707-3.14.0a0-68e279b/bm-20240707-pythonperf1-amd64-python-68e279b37aae3019979a-3.14.0a0-68e279b.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: unknown