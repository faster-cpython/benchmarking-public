
# Results vs. 3.11.0

- fork: faster-cpython
- ref: safe_decref
- machine: linux-x86_64
- commit hash: b17c8ef
- commit date: 2023-06-03
- overall geometric mean: 1.05x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230603-linux-x86_64-faster%2dcpython-safe_decref-3.13.0a0-b17c8ef |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| docutils       | 2.63 sec                                               | 2.67 sec: 1.02x slower                                                 |
| tornado_http   | 96.3 ms                                                | 95.5 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.00x slower                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230603-linux-x86_64-faster%2dcpython-safe_decref-3.13.0a0-b17c8ef |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pidigits       | 198 ms                                                 | 189 ms: 1.05x faster                                                   |
| nbody          | 93.1 ms                                                | 90.7 ms: 1.03x faster                                                  |
| float          | 77.2 ms                                                | 76.6 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230603-linux-x86_64-faster%2dcpython-safe_decref-3.13.0a0-b17c8ef |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.71 ms: 1.08x faster                                                  |
| regex_compile  | 138 ms                                                 | 136 ms: 1.01x faster                                                   |
| regex_v8       | 22.0 ms                                                | 22.9 ms: 1.04x slower                                                  |
| regex_dna      | 204 ms                                                 | 214 ms: 1.05x slower                                                   |
| Geometric mean | (ref)                                                  | 1.00x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230603-linux-x86_64-faster%2dcpython-safe_decref-3.13.0a0-b17c8ef |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.67 ms: 1.30x faster                                                  |
| unpickle_pure_python | 228 us                                                 | 215 us: 1.06x faster                                                   |
| json_loads           | 26.5 us                                                | 25.2 us: 1.05x faster                                                  |
| xml_etree_parse      | 158 ms                                                 | 153 ms: 1.03x faster                                                   |
| tomli_loads          | 2.22 sec                                               | 2.15 sec: 1.03x faster                                                 |
| pickle_dict          | 31.1 us                                                | 30.4 us: 1.02x faster                                                  |
| xml_etree_iterparse  | 104 ms                                                 | 103 ms: 1.01x faster                                                   |
| pickle_pure_python   | 306 us                                                 | 308 us: 1.01x slower                                                   |
| unpickle_list        | 4.91 us                                                | 4.99 us: 1.02x slower                                                  |
| pickle               | 10.1 us                                                | 10.6 us: 1.05x slower                                                  |
| xml_etree_process    | 53.9 ms                                                | 57.0 ms: 1.06x slower                                                  |
| xml_etree_generate   | 76.2 ms                                                | 83.5 ms: 1.10x slower                                                  |
| unpickle             | 13.7 us                                                | 15.0 us: 1.10x slower                                                  |
| pickle_list          | 4.11 us                                                | 4.57 us: 1.11x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.00x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230603-linux-x86_64-faster%2dcpython-safe_decref-3.13.0a0-b17c8ef |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.21 ms: 1.08x slower                                                  |
| python_startup_no_site | 6.01 ms                                                | 6.69 ms: 1.11x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.10x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230603-linux-x86_64-faster%2dcpython-safe_decref-3.13.0a0-b17c8ef |
|-----------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako      | 10.1 ms                                                | 10.6 ms: 1.05x slower                                                  |

All benchmarks:
===============

| Benchmark                | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230603-linux-x86_64-faster%2dcpython-safe_decref-3.13.0a0-b17c8ef |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols | 486 us                                                 | 141 us: 3.46x faster                                                   |
| generators               | 73.5 ms                                                | 29.3 ms: 2.51x faster                                                  |
| asyncio_tcp              | 922 ms                                                 | 508 ms: 1.81x faster                                                   |
| asyncio_tcp_ssl          | 3.14 sec                                               | 1.79 sec: 1.75x faster                                                 |
| json_dumps               | 12.6 ms                                                | 9.67 ms: 1.30x faster                                                  |
| mypy2                    | 420 ms                                                 | 335 ms: 1.26x faster                                                   |
| deltablue                | 3.67 ms                                                | 3.20 ms: 1.15x faster                                                  |
| chaos                    | 69.2 ms                                                | 60.9 ms: 1.14x faster                                                  |
| richards_super           | 56.8 ms                                                | 50.2 ms: 1.13x faster                                                  |
| coroutines               | 25.5 ms                                                | 22.7 ms: 1.12x faster                                                  |
| comprehensions           | 22.4 us                                                | 20.4 us: 1.10x faster                                                  |
| sqlglot_parse            | 1.40 ms                                                | 1.28 ms: 1.09x faster                                                  |
| regex_effbot             | 3.99 ms                                                | 3.71 ms: 1.08x faster                                                  |
| async_tree_none          | 526 ms                                                 | 489 ms: 1.08x faster                                                   |
| logging_silent           | 101 ns                                                 | 94.9 ns: 1.07x faster                                                  |
| sqlglot_transpile        | 1.70 ms                                                | 1.60 ms: 1.07x faster                                                  |
| hexiom                   | 6.37 ms                                                | 6.00 ms: 1.06x faster                                                  |
| unpickle_pure_python     | 228 us                                                 | 215 us: 1.06x faster                                                   |
| async_tree_io            | 1.30 sec                                               | 1.22 sec: 1.06x faster                                                 |
| async_tree_memoization   | 627 ms                                                 | 594 ms: 1.06x faster                                                   |
| go                       | 140 ms                                                 | 133 ms: 1.05x faster                                                   |
| json_loads               | 26.5 us                                                | 25.2 us: 1.05x faster                                                  |
| nqueens                  | 83.4 ms                                                | 79.4 ms: 1.05x faster                                                  |
| gc_traversal             | 4.02 ms                                                | 3.84 ms: 1.05x faster                                                  |
| coverage                 | 100 ms                                                 | 95.5 ms: 1.05x faster                                                  |
| pidigits                 | 198 ms                                                 | 189 ms: 1.05x faster                                                   |
| richards                 | 45.7 ms                                                | 43.9 ms: 1.04x faster                                                  |
| pycparser                | 1.18 sec                                               | 1.14 sec: 1.04x faster                                                 |
| xml_etree_parse          | 158 ms                                                 | 153 ms: 1.03x faster                                                   |
| tomli_loads              | 2.22 sec                                               | 2.15 sec: 1.03x faster                                                 |
| raytrace                 | 297 ms                                                 | 288 ms: 1.03x faster                                                   |
| sqlglot_normalize        | 108 ms                                                 | 105 ms: 1.03x faster                                                   |
| nbody                    | 93.1 ms                                                | 90.7 ms: 1.03x faster                                                  |
| logging_format           | 6.68 us                                                | 6.53 us: 1.02x faster                                                  |
| pickle_dict              | 31.1 us                                                | 30.4 us: 1.02x faster                                                  |
| json                     | 4.94 ms                                                | 4.85 ms: 1.02x faster                                                  |
| scimark_lu               | 110 ms                                                 | 108 ms: 1.02x faster                                                   |
| sqlglot_optimize         | 53.1 ms                                                | 52.4 ms: 1.01x faster                                                  |
| async_tree_cpu_io_mixed  | 739 ms                                                 | 730 ms: 1.01x faster                                                   |
| regex_compile            | 138 ms                                                 | 136 ms: 1.01x faster                                                   |
| xml_etree_iterparse      | 104 ms                                                 | 103 ms: 1.01x faster                                                   |
| tornado_http             | 96.3 ms                                                | 95.5 ms: 1.01x faster                                                  |
| float                    | 77.2 ms                                                | 76.6 ms: 1.01x faster                                                  |
| pprint_pformat           | 1.46 sec                                               | 1.46 sec: 1.00x slower                                                 |
| pathlib                  | 18.2 ms                                                | 18.3 ms: 1.01x slower                                                  |
| logging_simple           | 6.03 us                                                | 6.08 us: 1.01x slower                                                  |
| pickle_pure_python       | 306 us                                                 | 308 us: 1.01x slower                                                   |
| create_gc_cycles         | 1.49 ms                                                | 1.50 ms: 1.01x slower                                                  |
| unpickle_list            | 4.91 us                                                | 4.99 us: 1.02x slower                                                  |
| dulwich_log              | 63.7 ms                                                | 64.7 ms: 1.02x slower                                                  |
| deepcopy_memo            | 37.0 us                                                | 37.7 us: 1.02x slower                                                  |
| docutils                 | 2.63 sec                                               | 2.67 sec: 1.02x slower                                                 |
| deepcopy                 | 342 us                                                 | 350 us: 1.02x slower                                                   |
| mdp                      | 2.62 sec                                               | 2.68 sec: 1.02x slower                                                 |
| pprint_safe_repr         | 701 ms                                                 | 720 ms: 1.03x slower                                                   |
| crypto_pyaes             | 74.7 ms                                                | 76.8 ms: 1.03x slower                                                  |
| unpack_sequence          | 43.1 ns                                                | 44.4 ns: 1.03x slower                                                  |
| spectral_norm            | 100 ms                                                 | 103 ms: 1.03x slower                                                   |
| scimark_monte_carlo      | 68.1 ms                                                | 70.4 ms: 1.03x slower                                                  |
| regex_v8                 | 22.0 ms                                                | 22.9 ms: 1.04x slower                                                  |
| scimark_sparse_mat_mult  | 4.50 ms                                                | 4.71 ms: 1.05x slower                                                  |
| regex_dna                | 204 ms                                                 | 214 ms: 1.05x slower                                                   |
| mako                     | 10.1 ms                                                | 10.6 ms: 1.05x slower                                                  |
| pickle                   | 10.1 us                                                | 10.6 us: 1.05x slower                                                  |
| telco                    | 6.58 ms                                                | 6.96 ms: 1.06x slower                                                  |
| pyflate                  | 418 ms                                                 | 442 ms: 1.06x slower                                                   |
| xml_etree_process        | 53.9 ms                                                | 57.0 ms: 1.06x slower                                                  |
| scimark_fft              | 328 ms                                                 | 348 ms: 1.06x slower                                                   |
| deepcopy_reduce          | 2.94 us                                                | 3.16 us: 1.07x slower                                                  |
| python_startup           | 8.52 ms                                                | 9.21 ms: 1.08x slower                                                  |
| sqlite_synth             | 2.52 us                                                | 2.76 us: 1.09x slower                                                  |
| xml_etree_generate       | 76.2 ms                                                | 83.5 ms: 1.10x slower                                                  |
| unpickle                 | 13.7 us                                                | 15.0 us: 1.10x slower                                                  |
| pickle_list              | 4.11 us                                                | 4.57 us: 1.11x slower                                                  |
| python_startup_no_site   | 6.01 ms                                                | 6.69 ms: 1.11x slower                                                  |
| async_generators         | 368 ms                                                 | 446 ms: 1.21x slower                                                   |
| dask                     | 360 ms                                                 | 512 ms: 1.42x slower                                                   |
| Geometric mean           | (ref)                                                  | 1.05x faster                                                           |

Benchmark hidden because not significant (5): scimark_sor, meteor_contest, bench_thread_pool, bench_mp_pool, fannkuch
Ignored benchmarks (18) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
