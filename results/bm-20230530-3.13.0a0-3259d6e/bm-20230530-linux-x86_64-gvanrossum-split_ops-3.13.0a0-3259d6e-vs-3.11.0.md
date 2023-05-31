
# Results vs. 3.11.0

- fork: gvanrossum
- ref: split_ops
- machine: linux-x86_64
- commit hash: 3259d6e
- commit date: 2023-05-30
- overall geometric mean: 1.02x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230530-linux-x86_64-gvanrossum-split_ops-3.13.0a0-3259d6e |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| docutils       | 2.63 sec                                               | 2.74 sec: 1.04x slower                                         |
| tornado_http   | 96.3 ms                                                | 103 ms: 1.07x slower                                           |
| Geometric mean | (ref)                                                  | 1.05x slower                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230530-linux-x86_64-gvanrossum-split_ops-3.13.0a0-3259d6e |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| nbody          | 93.1 ms                                                | 89.1 ms: 1.05x faster                                          |
| pidigits       | 198 ms                                                 | 197 ms: 1.00x faster                                           |
| float          | 77.2 ms                                                | 81.8 ms: 1.06x slower                                          |
| Geometric mean | (ref)                                                  | 1.00x slower                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230530-linux-x86_64-gvanrossum-split_ops-3.13.0a0-3259d6e |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.71 ms: 1.08x faster                                          |
| regex_compile  | 138 ms                                                 | 146 ms: 1.05x slower                                           |
| regex_v8       | 22.0 ms                                                | 23.3 ms: 1.06x slower                                          |
| regex_dna      | 204 ms                                                 | 219 ms: 1.07x slower                                           |
| Geometric mean | (ref)                                                  | 1.03x slower                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230530-linux-x86_64-gvanrossum-split_ops-3.13.0a0-3259d6e |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.97 ms: 1.26x faster                                          |
| json_loads           | 26.5 us                                                | 25.0 us: 1.06x faster                                          |
| unpickle_pure_python | 228 us                                                 | 217 us: 1.05x faster                                           |
| xml_etree_parse      | 158 ms                                                 | 153 ms: 1.04x faster                                           |
| tomli_loads          | 2.22 sec                                               | 2.24 sec: 1.01x slower                                         |
| unpickle_list        | 4.91 us                                                | 4.98 us: 1.01x slower                                          |
| pickle_dict          | 31.1 us                                                | 31.7 us: 1.02x slower                                          |
| pickle_pure_python   | 306 us                                                 | 317 us: 1.04x slower                                           |
| pickle               | 10.1 us                                                | 10.5 us: 1.04x slower                                          |
| pickle_list          | 4.11 us                                                | 4.49 us: 1.09x slower                                          |
| xml_etree_process    | 53.9 ms                                                | 59.3 ms: 1.10x slower                                          |
| unpickle             | 13.7 us                                                | 15.1 us: 1.11x slower                                          |
| xml_etree_generate   | 76.2 ms                                                | 85.1 ms: 1.12x slower                                          |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                   |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230530-linux-x86_64-gvanrossum-split_ops-3.13.0a0-3259d6e |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.33 ms: 1.09x slower                                          |
| python_startup_no_site | 6.01 ms                                                | 6.79 ms: 1.13x slower                                          |
| Geometric mean         | (ref)                                                  | 1.11x slower                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230530-linux-x86_64-gvanrossum-split_ops-3.13.0a0-3259d6e |
|-----------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| mako      | 10.1 ms                                                | 10.7 ms: 1.06x slower                                          |

All benchmarks:
===============

| Benchmark                | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230530-linux-x86_64-gvanrossum-split_ops-3.13.0a0-3259d6e |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| typing_runtime_protocols | 486 us                                                 | 146 us: 3.33x faster                                           |
| generators               | 73.5 ms                                                | 31.5 ms: 2.33x faster                                          |
| asyncio_tcp              | 922 ms                                                 | 509 ms: 1.81x faster                                           |
| asyncio_tcp_ssl          | 3.14 sec                                               | 1.80 sec: 1.74x faster                                         |
| json_dumps               | 12.6 ms                                                | 9.97 ms: 1.26x faster                                          |
| mypy2                    | 420 ms                                                 | 347 ms: 1.21x faster                                           |
| coroutines               | 25.5 ms                                                | 22.5 ms: 1.13x faster                                          |
| richards_super           | 56.8 ms                                                | 50.6 ms: 1.12x faster                                          |
| gc_traversal             | 4.02 ms                                                | 3.61 ms: 1.11x faster                                          |
| comprehensions           | 22.4 us                                                | 20.6 us: 1.09x faster                                          |
| regex_effbot             | 3.99 ms                                                | 3.71 ms: 1.08x faster                                          |
| chaos                    | 69.2 ms                                                | 64.9 ms: 1.07x faster                                          |
| async_tree_none          | 526 ms                                                 | 495 ms: 1.06x faster                                           |
| json_loads               | 26.5 us                                                | 25.0 us: 1.06x faster                                          |
| async_tree_io            | 1.30 sec                                               | 1.22 sec: 1.06x faster                                         |
| unpickle_pure_python     | 228 us                                                 | 217 us: 1.05x faster                                           |
| async_tree_memoization   | 627 ms                                                 | 599 ms: 1.05x faster                                           |
| nbody                    | 93.1 ms                                                | 89.1 ms: 1.05x faster                                          |
| deltablue                | 3.67 ms                                                | 3.52 ms: 1.04x faster                                          |
| sqlglot_parse            | 1.40 ms                                                | 1.35 ms: 1.04x faster                                          |
| xml_etree_parse          | 158 ms                                                 | 153 ms: 1.04x faster                                           |
| go                       | 140 ms                                                 | 136 ms: 1.03x faster                                           |
| json                     | 4.94 ms                                                | 4.81 ms: 1.03x faster                                          |
| sqlglot_transpile        | 1.70 ms                                                | 1.67 ms: 1.02x faster                                          |
| coverage                 | 100 ms                                                 | 98.2 ms: 1.02x faster                                          |
| hexiom                   | 6.37 ms                                                | 6.27 ms: 1.02x faster                                          |
| meteor_contest           | 107 ms                                                 | 105 ms: 1.01x faster                                           |
| richards                 | 45.7 ms                                                | 45.2 ms: 1.01x faster                                          |
| logging_silent           | 101 ns                                                 | 100 ns: 1.01x faster                                           |
| pidigits                 | 198 ms                                                 | 197 ms: 1.00x faster                                           |
| tomli_loads              | 2.22 sec                                               | 2.24 sec: 1.01x slower                                         |
| raytrace                 | 297 ms                                                 | 300 ms: 1.01x slower                                           |
| deepcopy_memo            | 37.0 us                                                | 37.4 us: 1.01x slower                                          |
| fannkuch                 | 388 ms                                                 | 393 ms: 1.01x slower                                           |
| unpickle_list            | 4.91 us                                                | 4.98 us: 1.01x slower                                          |
| pickle_dict              | 31.1 us                                                | 31.7 us: 1.02x slower                                          |
| create_gc_cycles         | 1.49 ms                                                | 1.52 ms: 1.02x slower                                          |
| bench_thread_pool        | 819 us                                                 | 835 us: 1.02x slower                                           |
| pathlib                  | 18.2 ms                                                | 18.7 ms: 1.03x slower                                          |
| sqlglot_optimize         | 53.1 ms                                                | 54.5 ms: 1.03x slower                                          |
| sqlglot_normalize        | 108 ms                                                 | 111 ms: 1.03x slower                                           |
| mdp                      | 2.62 sec                                               | 2.71 sec: 1.03x slower                                         |
| pickle_pure_python       | 306 us                                                 | 317 us: 1.04x slower                                           |
| pickle                   | 10.1 us                                                | 10.5 us: 1.04x slower                                          |
| pprint_pformat           | 1.46 sec                                               | 1.52 sec: 1.04x slower                                         |
| scimark_lu               | 110 ms                                                 | 114 ms: 1.04x slower                                           |
| scimark_sor              | 118 ms                                                 | 123 ms: 1.04x slower                                           |
| docutils                 | 2.63 sec                                               | 2.74 sec: 1.04x slower                                         |
| logging_simple           | 6.03 us                                                | 6.31 us: 1.05x slower                                          |
| logging_format           | 6.68 us                                                | 6.99 us: 1.05x slower                                          |
| deepcopy                 | 342 us                                                 | 358 us: 1.05x slower                                           |
| telco                    | 6.58 ms                                                | 6.90 ms: 1.05x slower                                          |
| regex_compile            | 138 ms                                                 | 146 ms: 1.05x slower                                           |
| crypto_pyaes             | 74.7 ms                                                | 78.8 ms: 1.06x slower                                          |
| regex_v8                 | 22.0 ms                                                | 23.3 ms: 1.06x slower                                          |
| float                    | 77.2 ms                                                | 81.8 ms: 1.06x slower                                          |
| mako                     | 10.1 ms                                                | 10.7 ms: 1.06x slower                                          |
| scimark_monte_carlo      | 68.1 ms                                                | 72.3 ms: 1.06x slower                                          |
| pprint_safe_repr         | 701 ms                                                 | 748 ms: 1.07x slower                                           |
| tornado_http             | 96.3 ms                                                | 103 ms: 1.07x slower                                           |
| pyflate                  | 418 ms                                                 | 447 ms: 1.07x slower                                           |
| dulwich_log              | 63.7 ms                                                | 68.3 ms: 1.07x slower                                          |
| regex_dna                | 204 ms                                                 | 219 ms: 1.07x slower                                           |
| scimark_fft              | 328 ms                                                 | 353 ms: 1.08x slower                                           |
| spectral_norm            | 100 ms                                                 | 108 ms: 1.08x slower                                           |
| sqlite_synth             | 2.52 us                                                | 2.74 us: 1.09x slower                                          |
| pickle_list              | 4.11 us                                                | 4.49 us: 1.09x slower                                          |
| python_startup           | 8.52 ms                                                | 9.33 ms: 1.09x slower                                          |
| deepcopy_reduce          | 2.94 us                                                | 3.22 us: 1.09x slower                                          |
| xml_etree_process        | 53.9 ms                                                | 59.3 ms: 1.10x slower                                          |
| unpickle                 | 13.7 us                                                | 15.1 us: 1.11x slower                                          |
| scimark_sparse_mat_mult  | 4.50 ms                                                | 5.02 ms: 1.12x slower                                          |
| xml_etree_generate       | 76.2 ms                                                | 85.1 ms: 1.12x slower                                          |
| python_startup_no_site   | 6.01 ms                                                | 6.79 ms: 1.13x slower                                          |
| unpack_sequence          | 43.1 ns                                                | 51.8 ns: 1.20x slower                                          |
| async_generators         | 368 ms                                                 | 456 ms: 1.24x slower                                           |
| dask                     | 360 ms                                                 | 539 ms: 1.50x slower                                           |
| Geometric mean           | (ref)                                                  | 1.02x faster                                                   |

Benchmark hidden because not significant (5): pycparser, async_tree_cpu_io_mixed, nqueens, bench_mp_pool, xml_etree_iterparse
Ignored benchmarks (18) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
