
# Results vs. 3.11.0

- fork: python
- ref: v3.12.0b1
- machine: linux-x86_64
- commit hash: 5612078
- commit date: 2023-05-22
- overall geometric mean: 1.02x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230522-linux-x86_64-python-v3.12.0b1-3.12.0b1-5612078 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 268 ms: 1.04x slower                                       |
| docutils       | 2.63 sec                                               | 2.71 sec: 1.03x slower                                     |
| tornado_http   | 96.3 ms                                                | 99.2 ms: 1.03x slower                                      |
| Geometric mean | (ref)                                                  | 1.03x slower                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230522-linux-x86_64-python-v3.12.0b1-3.12.0b1-5612078 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| nbody          | 93.1 ms                                                | 88.9 ms: 1.05x faster                                      |
| pidigits       | 198 ms                                                 | 196 ms: 1.01x faster                                       |
| float          | 77.2 ms                                                | 80.7 ms: 1.04x slower                                      |
| Geometric mean | (ref)                                                  | 1.00x faster                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230522-linux-x86_64-python-v3.12.0b1-3.12.0b1-5612078 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.54 ms: 1.13x faster                                      |
| regex_v8       | 22.0 ms                                                | 21.8 ms: 1.01x faster                                      |
| regex_dna      | 204 ms                                                 | 208 ms: 1.02x slower                                       |
| regex_compile  | 138 ms                                                 | 144 ms: 1.04x slower                                       |
| Geometric mean | (ref)                                                  | 1.02x faster                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230522-linux-x86_64-python-v3.12.0b1-3.12.0b1-5612078 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.76 ms: 1.29x faster                                      |
| unpickle_pure_python | 228 us                                                 | 216 us: 1.06x faster                                       |
| json_loads           | 26.5 us                                                | 25.1 us: 1.06x faster                                      |
| xml_etree_parse      | 158 ms                                                 | 153 ms: 1.04x faster                                       |
| tomli_loads          | 2.22 sec                                               | 2.18 sec: 1.02x faster                                     |
| xml_etree_iterparse  | 104 ms                                                 | 103 ms: 1.01x faster                                       |
| pickle_pure_python   | 306 us                                                 | 312 us: 1.02x slower                                       |
| pickle               | 10.1 us                                                | 10.6 us: 1.05x slower                                      |
| unpickle_list        | 4.91 us                                                | 5.17 us: 1.05x slower                                      |
| pickle_dict          | 31.1 us                                                | 33.3 us: 1.07x slower                                      |
| unpickle             | 13.7 us                                                | 14.9 us: 1.09x slower                                      |
| xml_etree_process    | 53.9 ms                                                | 59.0 ms: 1.10x slower                                      |
| xml_etree_generate   | 76.2 ms                                                | 85.6 ms: 1.12x slower                                      |
| pickle_list          | 4.11 us                                                | 4.73 us: 1.15x slower                                      |
| Geometric mean       | (ref)                                                  | 1.01x slower                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230522-linux-x86_64-python-v3.12.0b1-3.12.0b1-5612078 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.34 ms: 1.10x slower                                      |
| python_startup_no_site | 6.01 ms                                                | 6.78 ms: 1.13x slower                                      |
| Geometric mean         | (ref)                                                  | 1.11x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230522-linux-x86_64-python-v3.12.0b1-3.12.0b1-5612078 |
|-----------|:------------------------------------------------------:|:----------------------------------------------------------:|
| mako      | 10.1 ms                                                | 10.8 ms: 1.08x slower                                      |

All benchmarks:
===============

| Benchmark                | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230522-linux-x86_64-python-v3.12.0b1-3.12.0b1-5612078 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| typing_runtime_protocols | 486 us                                                 | 140 us: 3.47x faster                                       |
| generators               | 73.5 ms                                                | 31.4 ms: 2.34x faster                                      |
| asyncio_tcp              | 922 ms                                                 | 513 ms: 1.80x faster                                       |
| asyncio_tcp_ssl          | 3.14 sec                                               | 1.80 sec: 1.74x faster                                     |
| json_dumps               | 12.6 ms                                                | 9.76 ms: 1.29x faster                                      |
| coroutines               | 25.5 ms                                                | 21.9 ms: 1.17x faster                                      |
| richards_super           | 56.8 ms                                                | 49.8 ms: 1.14x faster                                      |
| regex_effbot             | 3.99 ms                                                | 3.54 ms: 1.13x faster                                      |
| async_tree_none          | 526 ms                                                 | 469 ms: 1.12x faster                                       |
| async_tree_io            | 1.30 sec                                               | 1.16 sec: 1.12x faster                                     |
| async_tree_memoization   | 627 ms                                                 | 572 ms: 1.10x faster                                       |
| gc_traversal             | 4.02 ms                                                | 3.67 ms: 1.10x faster                                      |
| comprehensions           | 22.4 us                                                | 20.6 us: 1.09x faster                                      |
| chaos                    | 69.2 ms                                                | 64.6 ms: 1.07x faster                                      |
| deltablue                | 3.67 ms                                                | 3.44 ms: 1.07x faster                                      |
| unpickle_pure_python     | 228 us                                                 | 216 us: 1.06x faster                                       |
| json_loads               | 26.5 us                                                | 25.1 us: 1.06x faster                                      |
| sqlglot_parse            | 1.40 ms                                                | 1.33 ms: 1.05x faster                                      |
| richards                 | 45.7 ms                                                | 43.6 ms: 1.05x faster                                      |
| nbody                    | 93.1 ms                                                | 88.9 ms: 1.05x faster                                      |
| async_tree_cpu_io_mixed  | 739 ms                                                 | 708 ms: 1.04x faster                                       |
| hexiom                   | 6.37 ms                                                | 6.12 ms: 1.04x faster                                      |
| sqlglot_transpile        | 1.70 ms                                                | 1.64 ms: 1.04x faster                                      |
| xml_etree_parse          | 158 ms                                                 | 153 ms: 1.04x faster                                       |
| json                     | 4.94 ms                                                | 4.77 ms: 1.04x faster                                      |
| coverage                 | 100 ms                                                 | 96.8 ms: 1.03x faster                                      |
| go                       | 140 ms                                                 | 136 ms: 1.03x faster                                       |
| nqueens                  | 83.4 ms                                                | 81.4 ms: 1.02x faster                                      |
| tomli_loads              | 2.22 sec                                               | 2.18 sec: 1.02x faster                                     |
| fannkuch                 | 388 ms                                                 | 382 ms: 1.02x faster                                       |
| meteor_contest           | 107 ms                                                 | 105 ms: 1.01x faster                                       |
| regex_v8                 | 22.0 ms                                                | 21.8 ms: 1.01x faster                                      |
| pidigits                 | 198 ms                                                 | 196 ms: 1.01x faster                                       |
| xml_etree_iterparse      | 104 ms                                                 | 103 ms: 1.01x faster                                       |
| pathlib                  | 18.2 ms                                                | 18.3 ms: 1.00x slower                                      |
| raytrace                 | 297 ms                                                 | 298 ms: 1.01x slower                                       |
| create_gc_cycles         | 1.49 ms                                                | 1.50 ms: 1.01x slower                                      |
| sqlglot_normalize        | 108 ms                                                 | 109 ms: 1.01x slower                                       |
| bench_thread_pool        | 819 us                                                 | 827 us: 1.01x slower                                       |
| deepcopy_memo            | 37.0 us                                                | 37.6 us: 1.02x slower                                      |
| sqlglot_optimize         | 53.1 ms                                                | 54.1 ms: 1.02x slower                                      |
| pickle_pure_python       | 306 us                                                 | 312 us: 1.02x slower                                       |
| regex_dna                | 204 ms                                                 | 208 ms: 1.02x slower                                       |
| mdp                      | 2.62 sec                                               | 2.68 sec: 1.02x slower                                     |
| pprint_pformat           | 1.46 sec                                               | 1.50 sec: 1.03x slower                                     |
| tornado_http             | 96.3 ms                                                | 99.2 ms: 1.03x slower                                      |
| scimark_lu               | 110 ms                                                 | 113 ms: 1.03x slower                                       |
| docutils                 | 2.63 sec                                               | 2.71 sec: 1.03x slower                                     |
| 2to3                     | 259 ms                                                 | 268 ms: 1.04x slower                                       |
| sqlalchemy_imperative    | 17.9 ms                                                | 18.6 ms: 1.04x slower                                      |
| telco                    | 6.58 ms                                                | 6.84 ms: 1.04x slower                                      |
| regex_compile            | 138 ms                                                 | 144 ms: 1.04x slower                                       |
| scimark_sor              | 118 ms                                                 | 123 ms: 1.04x slower                                       |
| crypto_pyaes             | 74.7 ms                                                | 77.9 ms: 1.04x slower                                      |
| pprint_safe_repr         | 701 ms                                                 | 733 ms: 1.04x slower                                       |
| float                    | 77.2 ms                                                | 80.7 ms: 1.04x slower                                      |
| pickle                   | 10.1 us                                                | 10.6 us: 1.05x slower                                      |
| logging_simple           | 6.03 us                                                | 6.33 us: 1.05x slower                                      |
| sqlalchemy_declarative   | 138 ms                                                 | 145 ms: 1.05x slower                                       |
| unpickle_list            | 4.91 us                                                | 5.17 us: 1.05x slower                                      |
| deepcopy                 | 342 us                                                 | 361 us: 1.06x slower                                       |
| pyflate                  | 418 ms                                                 | 443 ms: 1.06x slower                                       |
| logging_format           | 6.68 us                                                | 7.09 us: 1.06x slower                                      |
| dulwich_log              | 63.7 ms                                                | 67.7 ms: 1.06x slower                                      |
| scimark_monte_carlo      | 68.1 ms                                                | 72.7 ms: 1.07x slower                                      |
| pickle_dict              | 31.1 us                                                | 33.3 us: 1.07x slower                                      |
| mako                     | 10.1 ms                                                | 10.8 ms: 1.08x slower                                      |
| sqlite_synth             | 2.52 us                                                | 2.72 us: 1.08x slower                                      |
| spectral_norm            | 100 ms                                                 | 108 ms: 1.08x slower                                       |
| scimark_fft              | 328 ms                                                 | 356 ms: 1.08x slower                                       |
| deepcopy_reduce          | 2.94 us                                                | 3.18 us: 1.08x slower                                      |
| unpickle                 | 13.7 us                                                | 14.9 us: 1.09x slower                                      |
| python_startup           | 8.52 ms                                                | 9.34 ms: 1.10x slower                                      |
| xml_etree_process        | 53.9 ms                                                | 59.0 ms: 1.10x slower                                      |
| unpack_sequence          | 43.1 ns                                                | 47.3 ns: 1.10x slower                                      |
| xml_etree_generate       | 76.2 ms                                                | 85.6 ms: 1.12x slower                                      |
| scimark_sparse_mat_mult  | 4.50 ms                                                | 5.05 ms: 1.12x slower                                      |
| python_startup_no_site   | 6.01 ms                                                | 6.78 ms: 1.13x slower                                      |
| pickle_list              | 4.11 us                                                | 4.73 us: 1.15x slower                                      |
| async_generators         | 368 ms                                                 | 449 ms: 1.22x slower                                       |
| dask                     | 360 ms                                                 | 535 ms: 1.49x slower                                       |
| Geometric mean           | (ref)                                                  | 1.02x faster                                               |

Benchmark hidden because not significant (4): logging_silent, bench_mp_pool, pycparser, mypy2
Ignored benchmarks (15) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
