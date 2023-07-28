
# Results vs. 3.11.0

- fork: illia-v
- ref: gh_102509
- machine: linux-x86_64
- commit hash: 3d240a8
- commit date: 2023-03-13
- overall geometric mean: 1.04x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230313-pythonperf2-x86_64-illia%2dv-gh_102509-3.12.0a6+-3d240a8 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 288 ms                                                       | 283 ms: 1.02x faster                                                 |
| chameleon      | 7.67 ms                                                      | 7.28 ms: 1.05x faster                                                |
| docutils       | 2.86 sec                                                     | 2.81 sec: 1.02x faster                                               |
| html5lib       | 72.9 ms                                                      | 68.5 ms: 1.06x faster                                                |
| tornado_http   | 122 ms                                                       | 117 ms: 1.04x faster                                                 |
| Geometric mean | (ref)                                                        | 1.04x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230313-pythonperf2-x86_64-illia%2dv-gh_102509-3.12.0a6+-3d240a8 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| nbody          | 90.7 ms                                                      | 83.3 ms: 1.09x faster                                                |
| float          | 74.2 ms                                                      | 72.3 ms: 1.03x faster                                                |
| pidigits       | 251 ms                                                       | 250 ms: 1.00x faster                                                 |
| Geometric mean | (ref)                                                        | 1.04x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230313-pythonperf2-x86_64-illia%2dv-gh_102509-3.12.0a6+-3d240a8 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 158 ms                                                       | 149 ms: 1.06x faster                                                 |
| regex_effbot   | 3.50 ms                                                      | 3.53 ms: 1.01x slower                                                |
| regex_v8       | 23.9 ms                                                      | 24.1 ms: 1.01x slower                                                |
| regex_dna      | 227 ms                                                       | 239 ms: 1.05x slower                                                 |
| Geometric mean | (ref)                                                        | 1.00x slower                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230313-pythonperf2-x86_64-illia%2dv-gh_102509-3.12.0a6+-3d240a8 |
|----------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| json_dumps           | 13.4 ms                                                      | 10.4 ms: 1.29x faster                                                |
| json_loads           | 28.7 us                                                      | 24.2 us: 1.19x faster                                                |
| unpickle_pure_python | 241 us                                                       | 206 us: 1.17x faster                                                 |
| xml_etree_parse      | 158 ms                                                       | 144 ms: 1.10x faster                                                 |
| tomli_loads          | 2.26 sec                                                     | 2.11 sec: 1.07x faster                                               |
| pickle_pure_python   | 319 us                                                       | 307 us: 1.04x faster                                                 |
| unpickle_list        | 4.53 us                                                      | 4.44 us: 1.02x faster                                                |
| pickle_list          | 3.83 us                                                      | 3.77 us: 1.02x faster                                                |
| unpickle             | 13.4 us                                                      | 13.2 us: 1.02x faster                                                |
| xml_etree_process    | 56.5 ms                                                      | 57.8 ms: 1.02x slower                                                |
| pickle_dict          | 30.8 us                                                      | 32.3 us: 1.05x slower                                                |
| pickle               | 9.64 us                                                      | 10.2 us: 1.05x slower                                                |
| xml_etree_generate   | 80.5 ms                                                      | 85.1 ms: 1.06x slower                                                |
| Geometric mean       | (ref)                                                        | 1.05x faster                                                         |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230313-pythonperf2-x86_64-illia%2dv-gh_102509-3.12.0a6+-3d240a8 |
|------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                      | 11.3 ms: 1.05x slower                                                |
| python_startup_no_site | 7.76 ms                                                      | 8.36 ms: 1.08x slower                                                |
| Geometric mean         | (ref)                                                        | 1.06x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230313-pythonperf2-x86_64-illia%2dv-gh_102509-3.12.0a6+-3d240a8 |
|-----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 11.0 ms                                                      | 9.99 ms: 1.10x faster                                                |
| genshi_xml      | 58.5 ms                                                      | 55.1 ms: 1.06x faster                                                |
| django_template | 40.2 ms                                                      | 39.6 ms: 1.02x faster                                                |
| Geometric mean  | (ref)                                                        | 1.04x faster                                                         |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230313-pythonperf2-x86_64-illia%2dv-gh_102509-3.12.0a6+-3d240a8 |
|--------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| asyncio_tcp              | 753 ms                                                       | 386 ms: 1.95x faster                                                 |
| asyncio_tcp_ssl          | 3.08 sec                                                     | 1.58 sec: 1.95x faster                                               |
| generators               | 56.0 ms                                                      | 37.2 ms: 1.51x faster                                                |
| json_dumps               | 13.4 ms                                                      | 10.4 ms: 1.29x faster                                                |
| deltablue                | 4.00 ms                                                      | 3.32 ms: 1.21x faster                                                |
| json_loads               | 28.7 us                                                      | 24.2 us: 1.19x faster                                                |
| unpickle_pure_python     | 241 us                                                       | 206 us: 1.17x faster                                                 |
| scimark_lu               | 115 ms                                                       | 100 ms: 1.14x faster                                                 |
| hexiom                   | 7.13 ms                                                      | 6.36 ms: 1.12x faster                                                |
| json                     | 5.65 ms                                                      | 5.07 ms: 1.11x faster                                                |
| raytrace                 | 317 ms                                                       | 288 ms: 1.10x faster                                                 |
| mako                     | 11.0 ms                                                      | 9.99 ms: 1.10x faster                                                |
| xml_etree_parse          | 158 ms                                                       | 144 ms: 1.10x faster                                                 |
| scimark_fft              | 285 ms                                                       | 261 ms: 1.09x faster                                                 |
| coroutines               | 27.6 ms                                                      | 25.3 ms: 1.09x faster                                                |
| nbody                    | 90.7 ms                                                      | 83.3 ms: 1.09x faster                                                |
| deepcopy_memo            | 38.8 us                                                      | 36.0 us: 1.08x faster                                                |
| tomli_loads              | 2.26 sec                                                     | 2.11 sec: 1.07x faster                                               |
| scimark_sparse_mat_mult  | 4.05 ms                                                      | 3.79 ms: 1.07x faster                                                |
| richards                 | 48.3 ms                                                      | 45.3 ms: 1.07x faster                                                |
| html5lib                 | 72.9 ms                                                      | 68.5 ms: 1.06x faster                                                |
| dulwich_log              | 68.4 ms                                                      | 64.3 ms: 1.06x faster                                                |
| genshi_xml               | 58.5 ms                                                      | 55.1 ms: 1.06x faster                                                |
| chaos                    | 80.9 ms                                                      | 76.1 ms: 1.06x faster                                                |
| logging_format           | 8.11 us                                                      | 7.65 us: 1.06x faster                                                |
| regex_compile            | 158 ms                                                       | 149 ms: 1.06x faster                                                 |
| coverage                 | 84.8 ms                                                      | 80.1 ms: 1.06x faster                                                |
| logging_simple           | 7.19 us                                                      | 6.80 us: 1.06x faster                                                |
| pyflate                  | 449 ms                                                       | 424 ms: 1.06x faster                                                 |
| chameleon                | 7.67 ms                                                      | 7.28 ms: 1.05x faster                                                |
| deepcopy_reduce          | 3.51 us                                                      | 3.34 us: 1.05x faster                                                |
| pprint_pformat           | 1.63 sec                                                     | 1.56 sec: 1.05x faster                                               |
| fannkuch                 | 429 ms                                                       | 409 ms: 1.05x faster                                                 |
| pycparser                | 1.32 sec                                                     | 1.26 sec: 1.05x faster                                               |
| sqlglot_normalize        | 126 ms                                                       | 120 ms: 1.05x faster                                                 |
| mdp                      | 2.75 sec                                                     | 2.62 sec: 1.05x faster                                               |
| spectral_norm            | 93.3 ms                                                      | 89.5 ms: 1.04x faster                                                |
| bench_thread_pool        | 1.01 ms                                                      | 971 us: 1.04x faster                                                 |
| pickle_pure_python       | 319 us                                                       | 307 us: 1.04x faster                                                 |
| pathlib                  | 19.1 ms                                                      | 18.4 ms: 1.04x faster                                                |
| tornado_http             | 122 ms                                                       | 117 ms: 1.04x faster                                                 |
| deepcopy                 | 399 us                                                       | 387 us: 1.03x faster                                                 |
| nqueens                  | 103 ms                                                       | 99.9 ms: 1.03x faster                                                |
| go                       | 164 ms                                                       | 159 ms: 1.03x faster                                                 |
| scimark_monte_carlo      | 68.2 ms                                                      | 66.4 ms: 1.03x faster                                                |
| sympy_expand             | 555 ms                                                       | 540 ms: 1.03x faster                                                 |
| richards_super           | 61.0 ms                                                      | 59.5 ms: 1.03x faster                                                |
| float                    | 74.2 ms                                                      | 72.3 ms: 1.03x faster                                                |
| sqlglot_optimize         | 59.8 ms                                                      | 58.4 ms: 1.02x faster                                                |
| async_tree_memoization   | 630 ms                                                       | 616 ms: 1.02x faster                                                 |
| pprint_safe_repr         | 784 ms                                                       | 768 ms: 1.02x faster                                                 |
| unpickle_list            | 4.53 us                                                      | 4.44 us: 1.02x faster                                                |
| docutils                 | 2.86 sec                                                     | 2.81 sec: 1.02x faster                                               |
| typing_runtime_protocols | 523 us                                                       | 513 us: 1.02x faster                                                 |
| sympy_integrate          | 25.8 ms                                                      | 25.3 ms: 1.02x faster                                                |
| pickle_list              | 3.83 us                                                      | 3.77 us: 1.02x faster                                                |
| unpickle                 | 13.4 us                                                      | 13.2 us: 1.02x faster                                                |
| meteor_contest           | 131 ms                                                       | 129 ms: 1.02x faster                                                 |
| django_template          | 40.2 ms                                                      | 39.6 ms: 1.02x faster                                                |
| 2to3                     | 288 ms                                                       | 283 ms: 1.02x faster                                                 |
| unpack_sequence          | 45.6 ns                                                      | 45.0 ns: 1.01x faster                                                |
| scimark_sor              | 111 ms                                                       | 110 ms: 1.01x faster                                                 |
| async_tree_none          | 519 ms                                                       | 512 ms: 1.01x faster                                                 |
| logging_silent           | 101 ns                                                       | 99.6 ns: 1.01x faster                                                |
| sympy_str                | 337 ms                                                       | 334 ms: 1.01x faster                                                 |
| crypto_pyaes             | 83.4 ms                                                      | 82.8 ms: 1.01x faster                                                |
| pidigits                 | 251 ms                                                       | 250 ms: 1.00x faster                                                 |
| sqlglot_transpile        | 1.92 ms                                                      | 1.93 ms: 1.01x slower                                                |
| regex_effbot             | 3.50 ms                                                      | 3.53 ms: 1.01x slower                                                |
| telco                    | 6.86 ms                                                      | 6.92 ms: 1.01x slower                                                |
| regex_v8                 | 23.9 ms                                                      | 24.1 ms: 1.01x slower                                                |
| sympy_sum                | 185 ms                                                       | 187 ms: 1.01x slower                                                 |
| xml_etree_process        | 56.5 ms                                                      | 57.8 ms: 1.02x slower                                                |
| sqlglot_parse            | 1.53 ms                                                      | 1.57 ms: 1.02x slower                                                |
| create_gc_cycles         | 1.61 ms                                                      | 1.65 ms: 1.02x slower                                                |
| gc_traversal             | 3.85 ms                                                      | 3.96 ms: 1.03x slower                                                |
| bench_mp_pool            | 4.62 ms                                                      | 4.77 ms: 1.03x slower                                                |
| sqlite_synth             | 2.50 us                                                      | 2.59 us: 1.04x slower                                                |
| thrift                   | 925 us                                                       | 960 us: 1.04x slower                                                 |
| pickle_dict              | 30.8 us                                                      | 32.3 us: 1.05x slower                                                |
| python_startup           | 10.8 ms                                                      | 11.3 ms: 1.05x slower                                                |
| regex_dna                | 227 ms                                                       | 239 ms: 1.05x slower                                                 |
| pickle                   | 9.64 us                                                      | 10.2 us: 1.05x slower                                                |
| xml_etree_generate       | 80.5 ms                                                      | 85.1 ms: 1.06x slower                                                |
| python_startup_no_site   | 7.76 ms                                                      | 8.36 ms: 1.08x slower                                                |
| comprehensions           | 24.6 us                                                      | 27.0 us: 1.10x slower                                                |
| async_generators         | 316 ms                                                       | 382 ms: 1.21x slower                                                 |
| dask                     | 410 ms                                                       | 566 ms: 1.38x slower                                                 |
| Geometric mean           | (ref)                                                        | 1.04x faster                                                         |

Benchmark hidden because not significant (4): async_tree_io, xml_etree_iterparse, genshi_text, async_tree_cpu_io_mixed
Ignored benchmarks (7) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, flaskblogging, gunicorn, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative
