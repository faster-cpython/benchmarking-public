
# Results vs. 3.10.4

- fork: faster-cpython
- ref: incremental_gc
- machine: linux-x86_64
- commit hash: 5027c77
- commit date: 2023-08-11
- overall geometric mean: 1.35x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230811-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-5027c77 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| docutils       | 3.17 sec                                               | 2.38 sec: 1.33x faster                                                    |
| tornado_http   | 127 ms                                                 | 94.1 ms: 1.35x faster                                                     |
| Geometric mean | (ref)                                                  | 1.34x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230811-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-5027c77 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 92.9 ms: 1.52x faster                                                     |
| float          | 111 ms                                                 | 72.7 ms: 1.52x faster                                                     |
| pidigits       | 190 ms                                                 | 189 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                  | 1.33x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230811-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-5027c77 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 137 ms: 1.29x faster                                                      |
| regex_v8       | 25.0 ms                                                | 22.4 ms: 1.12x faster                                                     |
| regex_dna      | 222 ms                                                 | 210 ms: 1.06x faster                                                      |
| regex_effbot   | 3.23 ms                                                | 3.66 ms: 1.14x slower                                                     |
| Geometric mean | (ref)                                                  | 1.08x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230811-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-5027c77 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 299 us: 1.52x faster                                                      |
| unpickle_pure_python | 300 us                                                 | 212 us: 1.42x faster                                                      |
| json_dumps           | 13.5 ms                                                | 9.76 ms: 1.39x faster                                                     |
| xml_etree_process    | 74.9 ms                                                | 56.6 ms: 1.32x faster                                                     |
| tomli_loads          | 2.92 sec                                               | 2.30 sec: 1.27x faster                                                    |
| xml_etree_iterparse  | 111 ms                                                 | 94.0 ms: 1.19x faster                                                     |
| xml_etree_parse      | 163 ms                                                 | 140 ms: 1.17x faster                                                      |
| xml_etree_generate   | 94.2 ms                                                | 80.9 ms: 1.16x faster                                                     |
| json_loads           | 28.8 us                                                | 25.4 us: 1.13x faster                                                     |
| pickle_list          | 4.56 us                                                | 4.61 us: 1.01x slower                                                     |
| pickle               | 10.3 us                                                | 10.6 us: 1.03x slower                                                     |
| unpickle             | 14.1 us                                                | 15.0 us: 1.06x slower                                                     |
| unpickle_list        | 4.82 us                                                | 5.13 us: 1.06x slower                                                     |
| pickle_dict          | 27.3 us                                                | 31.5 us: 1.16x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.15x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230811-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-5027c77 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.30 ms: 1.52x faster                                                     |
| python_startup_no_site | 5.82 ms                                                | 6.79 ms: 1.17x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.14x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230811-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-5027c77 |
|-----------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako      | 14.8 ms                                                | 10.7 ms: 1.37x faster                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230811-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-5027c77 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols | 510 us                                                 | 144 us: 3.54x faster                                                      |
| async_tree_io            | 1.77 sec                                               | 562 ms: 3.16x faster                                                      |
| generators               | 76.8 ms                                                | 28.0 ms: 2.74x faster                                                     |
| async_tree_none          | 717 ms                                                 | 274 ms: 2.62x faster                                                      |
| async_tree_memoization   | 854 ms                                                 | 337 ms: 2.53x faster                                                      |
| deltablue                | 7.42 ms                                                | 3.08 ms: 2.41x faster                                                     |
| asyncio_tcp              | 925 ms                                                 | 483 ms: 1.91x faster                                                      |
| async_tree_cpu_io_mixed  | 951 ms                                                 | 498 ms: 1.91x faster                                                      |
| chaos                    | 106 ms                                                 | 58.9 ms: 1.80x faster                                                     |
| raytrace                 | 464 ms                                                 | 266 ms: 1.74x faster                                                      |
| logging_silent           | 175 ns                                                 | 103 ns: 1.69x faster                                                      |
| richards_super           | 90.7 ms                                                | 53.7 ms: 1.69x faster                                                     |
| asyncio_tcp_ssl          | 3.01 sec                                               | 1.78 sec: 1.69x faster                                                    |
| go                       | 229 ms                                                 | 137 ms: 1.68x faster                                                      |
| crypto_pyaes             | 118 ms                                                 | 71.5 ms: 1.66x faster                                                     |
| sqlglot_parse            | 2.06 ms                                                | 1.28 ms: 1.61x faster                                                     |
| scimark_monte_carlo      | 108 ms                                                 | 67.3 ms: 1.61x faster                                                     |
| scimark_sor              | 197 ms                                                 | 122 ms: 1.61x faster                                                      |
| richards                 | 74.9 ms                                                | 46.6 ms: 1.61x faster                                                     |
| hexiom                   | 9.53 ms                                                | 6.04 ms: 1.58x faster                                                     |
| pyflate                  | 673 ms                                                 | 438 ms: 1.54x faster                                                      |
| sqlglot_transpile        | 2.45 ms                                                | 1.60 ms: 1.53x faster                                                     |
| nbody                    | 142 ms                                                 | 92.9 ms: 1.52x faster                                                     |
| python_startup           | 14.2 ms                                                | 9.30 ms: 1.52x faster                                                     |
| pickle_pure_python       | 455 us                                                 | 299 us: 1.52x faster                                                      |
| float                    | 111 ms                                                 | 72.7 ms: 1.52x faster                                                     |
| scimark_lu               | 163 ms                                                 | 112 ms: 1.46x faster                                                      |
| unpickle_pure_python     | 300 us                                                 | 212 us: 1.42x faster                                                      |
| pycparser                | 1.50 sec                                               | 1.06 sec: 1.42x faster                                                    |
| coroutines               | 31.8 ms                                                | 22.5 ms: 1.41x faster                                                     |
| json_dumps               | 13.5 ms                                                | 9.76 ms: 1.39x faster                                                     |
| spectral_norm            | 150 ms                                                 | 108 ms: 1.38x faster                                                      |
| logging_format           | 8.91 us                                                | 6.44 us: 1.38x faster                                                     |
| deepcopy_memo            | 52.3 us                                                | 38.0 us: 1.38x faster                                                     |
| mako                     | 14.8 ms                                                | 10.7 ms: 1.37x faster                                                     |
| logging_simple           | 8.07 us                                                | 5.89 us: 1.37x faster                                                     |
| tornado_http             | 127 ms                                                 | 94.1 ms: 1.35x faster                                                     |
| pprint_pformat           | 1.99 sec                                               | 1.47 sec: 1.35x faster                                                    |
| pprint_safe_repr         | 955 ms                                                 | 716 ms: 1.33x faster                                                      |
| docutils                 | 3.17 sec                                               | 2.38 sec: 1.33x faster                                                    |
| unpack_sequence          | 64.7 ns                                                | 48.7 ns: 1.33x faster                                                     |
| comprehensions           | 26.8 us                                                | 20.3 us: 1.32x faster                                                     |
| xml_etree_process        | 74.9 ms                                                | 56.6 ms: 1.32x faster                                                     |
| regex_compile            | 177 ms                                                 | 137 ms: 1.29x faster                                                      |
| sqlglot_normalize        | 135 ms                                                 | 106 ms: 1.28x faster                                                      |
| tomli_loads              | 2.92 sec                                               | 2.30 sec: 1.27x faster                                                    |
| mypy2                    | 428 ms                                                 | 338 ms: 1.27x faster                                                      |
| deepcopy                 | 442 us                                                 | 355 us: 1.25x faster                                                      |
| sqlglot_optimize         | 65.3 ms                                                | 52.9 ms: 1.24x faster                                                     |
| fannkuch                 | 486 ms                                                 | 395 ms: 1.23x faster                                                      |
| nqueens                  | 100 ms                                                 | 81.4 ms: 1.23x faster                                                     |
| create_gc_cycles         | 1.67 ms                                                | 1.37 ms: 1.22x faster                                                     |
| deepcopy_reduce          | 3.82 us                                                | 3.21 us: 1.19x faster                                                     |
| xml_etree_iterparse      | 111 ms                                                 | 94.0 ms: 1.19x faster                                                     |
| scimark_fft              | 424 ms                                                 | 361 ms: 1.17x faster                                                      |
| xml_etree_parse          | 163 ms                                                 | 140 ms: 1.17x faster                                                      |
| xml_etree_generate       | 94.2 ms                                                | 80.9 ms: 1.16x faster                                                     |
| dulwich_log              | 75.9 ms                                                | 66.0 ms: 1.15x faster                                                     |
| bench_thread_pool        | 947 us                                                 | 828 us: 1.14x faster                                                      |
| scimark_sparse_mat_mult  | 5.45 ms                                                | 4.78 ms: 1.14x faster                                                     |
| json_loads               | 28.8 us                                                | 25.4 us: 1.13x faster                                                     |
| regex_v8                 | 25.0 ms                                                | 22.4 ms: 1.12x faster                                                     |
| json                     | 5.42 ms                                                | 4.85 ms: 1.12x faster                                                     |
| gc_traversal             | 3.84 ms                                                | 3.46 ms: 1.11x faster                                                     |
| meteor_contest           | 115 ms                                                 | 106 ms: 1.09x faster                                                      |
| pathlib                  | 20.0 ms                                                | 18.7 ms: 1.07x faster                                                     |
| sqlite_synth             | 2.93 us                                                | 2.74 us: 1.07x faster                                                     |
| regex_dna                | 222 ms                                                 | 210 ms: 1.06x faster                                                      |
| mdp                      | 2.82 sec                                               | 2.72 sec: 1.04x faster                                                    |
| async_generators         | 425 ms                                                 | 416 ms: 1.02x faster                                                      |
| pidigits                 | 190 ms                                                 | 189 ms: 1.01x faster                                                      |
| bench_mp_pool            | 24.0 ms                                                | 24.0 ms: 1.00x slower                                                     |
| pickle_list              | 4.56 us                                                | 4.61 us: 1.01x slower                                                     |
| pickle                   | 10.3 us                                                | 10.6 us: 1.03x slower                                                     |
| unpickle                 | 14.1 us                                                | 15.0 us: 1.06x slower                                                     |
| unpickle_list            | 4.82 us                                                | 5.13 us: 1.06x slower                                                     |
| regex_effbot             | 3.23 ms                                                | 3.66 ms: 1.14x slower                                                     |
| dask                     | 423 ms                                                 | 484 ms: 1.15x slower                                                      |
| pickle_dict              | 27.3 us                                                | 31.5 us: 1.16x slower                                                     |
| python_startup_no_site   | 5.82 ms                                                | 6.79 ms: 1.17x slower                                                     |
| telco                    | 6.54 ms                                                | 8.00 ms: 1.22x slower                                                     |
| coverage                 | 72.8 ms                                                | 94.3 ms: 1.29x slower                                                     |
| Geometric mean           | (ref)                                                  | 1.35x faster                                                              |
Ignored benchmarks (18) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.28x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.24x
