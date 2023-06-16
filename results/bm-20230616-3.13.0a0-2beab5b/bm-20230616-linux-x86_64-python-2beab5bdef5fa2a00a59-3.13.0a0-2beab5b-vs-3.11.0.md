
# Results vs. 3.11.0

- fork: python
- ref: 2beab5bdef5fa2a00a59
- machine: linux-x86_64
- commit hash: 2beab5b
- commit date: 2023-06-16
- overall geometric mean: 1.05x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230616-linux-x86_64-python-2beab5bdef5fa2a00a59-3.13.0a0-2beab5b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| docutils       | 2.63 sec                                               | 2.64 sec: 1.01x slower                                                |
| Geometric mean | (ref)                                                  | 1.01x slower                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230616-linux-x86_64-python-2beab5bdef5fa2a00a59-3.13.0a0-2beab5b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 198 ms                                                 | 192 ms: 1.03x faster                                                  |
| nbody          | 93.1 ms                                                | 90.7 ms: 1.03x faster                                                 |
| float          | 77.2 ms                                                | 79.9 ms: 1.03x slower                                                 |
| Geometric mean | (ref)                                                  | 1.01x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230616-linux-x86_64-python-2beab5bdef5fa2a00a59-3.13.0a0-2beab5b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 138 ms                                                 | 136 ms: 1.02x faster                                                  |
| regex_v8       | 22.0 ms                                                | 22.3 ms: 1.01x slower                                                 |
| regex_effbot   | 3.99 ms                                                | 4.12 ms: 1.03x slower                                                 |
| Geometric mean | (ref)                                                  | 1.01x slower                                                          |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230616-linux-x86_64-python-2beab5bdef5fa2a00a59-3.13.0a0-2beab5b |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.70 ms: 1.30x faster                                                 |
| unpickle_pure_python | 228 us                                                 | 212 us: 1.08x faster                                                  |
| json_loads           | 26.5 us                                                | 25.0 us: 1.06x faster                                                 |
| xml_etree_parse      | 158 ms                                                 | 154 ms: 1.03x faster                                                  |
| tomli_loads          | 2.22 sec                                               | 2.18 sec: 1.02x faster                                                |
| pickle_pure_python   | 306 us                                                 | 309 us: 1.01x slower                                                  |
| unpickle_list        | 4.91 us                                                | 5.00 us: 1.02x slower                                                 |
| pickle_dict          | 31.1 us                                                | 32.2 us: 1.03x slower                                                 |
| pickle               | 10.1 us                                                | 10.7 us: 1.06x slower                                                 |
| xml_etree_process    | 53.9 ms                                                | 57.3 ms: 1.06x slower                                                 |
| unpickle             | 13.7 us                                                | 14.9 us: 1.09x slower                                                 |
| xml_etree_generate   | 76.2 ms                                                | 83.6 ms: 1.10x slower                                                 |
| pickle_list          | 4.11 us                                                | 4.62 us: 1.12x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.00x slower                                                          |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230616-linux-x86_64-python-2beab5bdef5fa2a00a59-3.13.0a0-2beab5b |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.14 ms: 1.07x slower                                                 |
| python_startup_no_site | 6.01 ms                                                | 6.63 ms: 1.10x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.09x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230616-linux-x86_64-python-2beab5bdef5fa2a00a59-3.13.0a0-2beab5b |
|-----------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako      | 10.1 ms                                                | 10.7 ms: 1.06x slower                                                 |

All benchmarks:
===============

| Benchmark                | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230616-linux-x86_64-python-2beab5bdef5fa2a00a59-3.13.0a0-2beab5b |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 486 us                                                 | 147 us: 3.30x faster                                                  |
| generators               | 73.5 ms                                                | 29.0 ms: 2.53x faster                                                 |
| asyncio_tcp              | 922 ms                                                 | 508 ms: 1.81x faster                                                  |
| asyncio_tcp_ssl          | 3.14 sec                                               | 1.79 sec: 1.76x faster                                                |
| json_dumps               | 12.6 ms                                                | 9.70 ms: 1.30x faster                                                 |
| mypy2                    | 420 ms                                                 | 335 ms: 1.25x faster                                                  |
| coroutines               | 25.5 ms                                                | 21.8 ms: 1.17x faster                                                 |
| chaos                    | 69.2 ms                                                | 60.7 ms: 1.14x faster                                                 |
| deltablue                | 3.67 ms                                                | 3.24 ms: 1.13x faster                                                 |
| richards_super           | 56.8 ms                                                | 50.2 ms: 1.13x faster                                                 |
| comprehensions           | 22.4 us                                                | 20.2 us: 1.11x faster                                                 |
| async_tree_none          | 526 ms                                                 | 479 ms: 1.10x faster                                                  |
| async_tree_io            | 1.30 sec                                               | 1.20 sec: 1.08x faster                                                |
| sqlglot_parse            | 1.40 ms                                                | 1.30 ms: 1.08x faster                                                 |
| unpickle_pure_python     | 228 us                                                 | 212 us: 1.08x faster                                                  |
| coverage                 | 100 ms                                                 | 93.3 ms: 1.07x faster                                                 |
| async_tree_memoization   | 627 ms                                                 | 586 ms: 1.07x faster                                                  |
| hexiom                   | 6.37 ms                                                | 5.97 ms: 1.07x faster                                                 |
| nqueens                  | 83.4 ms                                                | 78.2 ms: 1.07x faster                                                 |
| json_loads               | 26.5 us                                                | 25.0 us: 1.06x faster                                                 |
| sqlglot_transpile        | 1.70 ms                                                | 1.62 ms: 1.05x faster                                                 |
| go                       | 140 ms                                                 | 134 ms: 1.05x faster                                                  |
| json                     | 4.94 ms                                                | 4.73 ms: 1.05x faster                                                 |
| richards                 | 45.7 ms                                                | 43.9 ms: 1.04x faster                                                 |
| pycparser                | 1.18 sec                                               | 1.14 sec: 1.03x faster                                                |
| pidigits                 | 198 ms                                                 | 192 ms: 1.03x faster                                                  |
| gc_traversal             | 4.02 ms                                                | 3.90 ms: 1.03x faster                                                 |
| mdp                      | 2.62 sec                                               | 2.54 sec: 1.03x faster                                                |
| nbody                    | 93.1 ms                                                | 90.7 ms: 1.03x faster                                                 |
| xml_etree_parse          | 158 ms                                                 | 154 ms: 1.03x faster                                                  |
| logging_silent           | 101 ns                                                 | 98.7 ns: 1.02x faster                                                 |
| async_tree_cpu_io_mixed  | 739 ms                                                 | 722 ms: 1.02x faster                                                  |
| meteor_contest           | 107 ms                                                 | 104 ms: 1.02x faster                                                  |
| raytrace                 | 297 ms                                                 | 290 ms: 1.02x faster                                                  |
| tomli_loads              | 2.22 sec                                               | 2.18 sec: 1.02x faster                                                |
| scimark_lu               | 110 ms                                                 | 108 ms: 1.02x faster                                                  |
| regex_compile            | 138 ms                                                 | 136 ms: 1.02x faster                                                  |
| fannkuch                 | 388 ms                                                 | 382 ms: 1.01x faster                                                  |
| pprint_pformat           | 1.46 sec                                               | 1.44 sec: 1.01x faster                                                |
| logging_format           | 6.68 us                                                | 6.59 us: 1.01x faster                                                 |
| logging_simple           | 6.03 us                                                | 5.96 us: 1.01x faster                                                 |
| sqlglot_normalize        | 108 ms                                                 | 107 ms: 1.01x faster                                                  |
| bench_thread_pool        | 819 us                                                 | 816 us: 1.00x faster                                                  |
| sqlglot_optimize         | 53.1 ms                                                | 53.3 ms: 1.00x slower                                                 |
| docutils                 | 2.63 sec                                               | 2.64 sec: 1.01x slower                                                |
| regex_v8                 | 22.0 ms                                                | 22.3 ms: 1.01x slower                                                 |
| pickle_pure_python       | 306 us                                                 | 309 us: 1.01x slower                                                  |
| create_gc_cycles         | 1.49 ms                                                | 1.51 ms: 1.01x slower                                                 |
| pprint_safe_repr         | 701 ms                                                 | 711 ms: 1.01x slower                                                  |
| dulwich_log              | 63.7 ms                                                | 64.7 ms: 1.02x slower                                                 |
| deepcopy                 | 342 us                                                 | 348 us: 1.02x slower                                                  |
| pathlib                  | 18.2 ms                                                | 18.5 ms: 1.02x slower                                                 |
| unpickle_list            | 4.91 us                                                | 5.00 us: 1.02x slower                                                 |
| scimark_sparse_mat_mult  | 4.50 ms                                                | 4.58 ms: 1.02x slower                                                 |
| deepcopy_memo            | 37.0 us                                                | 37.7 us: 1.02x slower                                                 |
| telco                    | 6.58 ms                                                | 6.72 ms: 1.02x slower                                                 |
| crypto_pyaes             | 74.7 ms                                                | 76.3 ms: 1.02x slower                                                 |
| regex_effbot             | 3.99 ms                                                | 4.12 ms: 1.03x slower                                                 |
| pickle_dict              | 31.1 us                                                | 32.2 us: 1.03x slower                                                 |
| float                    | 77.2 ms                                                | 79.9 ms: 1.03x slower                                                 |
| spectral_norm            | 100 ms                                                 | 104 ms: 1.04x slower                                                  |
| scimark_monte_carlo      | 68.1 ms                                                | 70.8 ms: 1.04x slower                                                 |
| pyflate                  | 418 ms                                                 | 440 ms: 1.05x slower                                                  |
| mako                     | 10.1 ms                                                | 10.7 ms: 1.06x slower                                                 |
| scimark_fft              | 328 ms                                                 | 348 ms: 1.06x slower                                                  |
| unpack_sequence          | 43.1 ns                                                | 45.7 ns: 1.06x slower                                                 |
| pickle                   | 10.1 us                                                | 10.7 us: 1.06x slower                                                 |
| xml_etree_process        | 53.9 ms                                                | 57.3 ms: 1.06x slower                                                 |
| deepcopy_reduce          | 2.94 us                                                | 3.13 us: 1.06x slower                                                 |
| python_startup           | 8.52 ms                                                | 9.14 ms: 1.07x slower                                                 |
| unpickle                 | 13.7 us                                                | 14.9 us: 1.09x slower                                                 |
| sqlite_synth             | 2.52 us                                                | 2.75 us: 1.09x slower                                                 |
| xml_etree_generate       | 76.2 ms                                                | 83.6 ms: 1.10x slower                                                 |
| python_startup_no_site   | 6.01 ms                                                | 6.63 ms: 1.10x slower                                                 |
| pickle_list              | 4.11 us                                                | 4.62 us: 1.12x slower                                                 |
| async_generators         | 368 ms                                                 | 458 ms: 1.24x slower                                                  |
| dask                     | 360 ms                                                 | 515 ms: 1.43x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.05x faster                                                          |

Benchmark hidden because not significant (5): scimark_sor, xml_etree_iterparse, bench_mp_pool, regex_dna, tornado_http
Ignored benchmarks (18) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
