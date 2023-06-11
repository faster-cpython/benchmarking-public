
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 3a314f7
- commit date: 2023-06-10
- overall geometric mean: 1.04x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230610-linux-x86_64-python-main-3.13.0a0-3a314f7 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| docutils       | 2.63 sec                                               | 2.68 sec: 1.02x slower                                |
| Geometric mean | (ref)                                                  | 1.01x slower                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230610-linux-x86_64-python-main-3.13.0a0-3a314f7 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| pidigits       | 198 ms                                                 | 196 ms: 1.01x faster                                  |
| float          | 77.2 ms                                                | 79.7 ms: 1.03x slower                                 |
| Geometric mean | (ref)                                                  | 1.01x slower                                          |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230610-linux-x86_64-python-main-3.13.0a0-3a314f7 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.56 ms: 1.12x faster                                 |
| regex_compile  | 138 ms                                                 | 137 ms: 1.01x faster                                  |
| regex_v8       | 22.0 ms                                                | 23.0 ms: 1.04x slower                                 |
| regex_dna      | 204 ms                                                 | 215 ms: 1.05x slower                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230610-linux-x86_64-python-main-3.13.0a0-3a314f7 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.88 ms: 1.27x faster                                 |
| unpickle_pure_python | 228 us                                                 | 212 us: 1.08x faster                                  |
| json_loads           | 26.5 us                                                | 25.3 us: 1.05x faster                                 |
| xml_etree_parse      | 158 ms                                                 | 152 ms: 1.04x faster                                  |
| xml_etree_iterparse  | 104 ms                                                 | 103 ms: 1.01x faster                                  |
| tomli_loads          | 2.22 sec                                               | 2.21 sec: 1.01x faster                                |
| unpickle_list        | 4.91 us                                                | 4.94 us: 1.01x slower                                 |
| xml_etree_process    | 53.9 ms                                                | 57.4 ms: 1.07x slower                                 |
| pickle               | 10.1 us                                                | 10.8 us: 1.07x slower                                 |
| xml_etree_generate   | 76.2 ms                                                | 83.8 ms: 1.10x slower                                 |
| pickle_list          | 4.11 us                                                | 4.55 us: 1.11x slower                                 |
| unpickle             | 13.7 us                                                | 15.3 us: 1.12x slower                                 |
| Geometric mean       | (ref)                                                  | 1.00x slower                                          |

Benchmark hidden because not significant (2): pickle_pure_python, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230610-linux-x86_64-python-main-3.13.0a0-3a314f7 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.19 ms: 1.08x slower                                 |
| python_startup_no_site | 6.01 ms                                                | 6.68 ms: 1.11x slower                                 |
| Geometric mean         | (ref)                                                  | 1.09x slower                                          |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230610-linux-x86_64-python-main-3.13.0a0-3a314f7 |
|-----------|:------------------------------------------------------:|:-----------------------------------------------------:|
| mako      | 10.1 ms                                                | 10.5 ms: 1.04x slower                                 |

All benchmarks:
===============

| Benchmark                | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230610-linux-x86_64-python-main-3.13.0a0-3a314f7 |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| typing_runtime_protocols | 486 us                                                 | 143 us: 3.40x faster                                  |
| generators               | 73.5 ms                                                | 28.7 ms: 2.56x faster                                 |
| asyncio_tcp              | 922 ms                                                 | 504 ms: 1.83x faster                                  |
| asyncio_tcp_ssl          | 3.14 sec                                               | 1.78 sec: 1.76x faster                                |
| json_dumps               | 12.6 ms                                                | 9.88 ms: 1.27x faster                                 |
| mypy2                    | 420 ms                                                 | 336 ms: 1.25x faster                                  |
| deltablue                | 3.67 ms                                                | 3.22 ms: 1.14x faster                                 |
| coroutines               | 25.5 ms                                                | 22.5 ms: 1.14x faster                                 |
| richards_super           | 56.8 ms                                                | 50.5 ms: 1.12x faster                                 |
| regex_effbot             | 3.99 ms                                                | 3.56 ms: 1.12x faster                                 |
| chaos                    | 69.2 ms                                                | 61.8 ms: 1.12x faster                                 |
| comprehensions           | 22.4 us                                                | 20.4 us: 1.10x faster                                 |
| coverage                 | 100 ms                                                 | 92.4 ms: 1.08x faster                                 |
| async_tree_none          | 526 ms                                                 | 488 ms: 1.08x faster                                  |
| sqlglot_parse            | 1.40 ms                                                | 1.30 ms: 1.08x faster                                 |
| async_tree_io            | 1.30 sec                                               | 1.20 sec: 1.08x faster                                |
| unpickle_pure_python     | 228 us                                                 | 212 us: 1.08x faster                                  |
| async_tree_memoization   | 627 ms                                                 | 590 ms: 1.06x faster                                  |
| logging_silent           | 101 ns                                                 | 95.4 ns: 1.06x faster                                 |
| hexiom                   | 6.37 ms                                                | 6.03 ms: 1.06x faster                                 |
| sqlglot_transpile        | 1.70 ms                                                | 1.62 ms: 1.05x faster                                 |
| nqueens                  | 83.4 ms                                                | 79.7 ms: 1.05x faster                                 |
| json_loads               | 26.5 us                                                | 25.3 us: 1.05x faster                                 |
| gc_traversal             | 4.02 ms                                                | 3.85 ms: 1.04x faster                                 |
| xml_etree_parse          | 158 ms                                                 | 152 ms: 1.04x faster                                  |
| logging_format           | 6.68 us                                                | 6.46 us: 1.03x faster                                 |
| pycparser                | 1.18 sec                                               | 1.14 sec: 1.03x faster                                |
| richards                 | 45.7 ms                                                | 44.3 ms: 1.03x faster                                 |
| go                       | 140 ms                                                 | 136 ms: 1.03x faster                                  |
| mdp                      | 2.62 sec                                               | 2.55 sec: 1.03x faster                                |
| meteor_contest           | 107 ms                                                 | 104 ms: 1.02x faster                                  |
| raytrace                 | 297 ms                                                 | 291 ms: 1.02x faster                                  |
| json                     | 4.94 ms                                                | 4.86 ms: 1.02x faster                                 |
| async_tree_cpu_io_mixed  | 739 ms                                                 | 728 ms: 1.01x faster                                  |
| xml_etree_iterparse      | 104 ms                                                 | 103 ms: 1.01x faster                                  |
| logging_simple           | 6.03 us                                                | 5.98 us: 1.01x faster                                 |
| scimark_lu               | 110 ms                                                 | 109 ms: 1.01x faster                                  |
| deepcopy_memo            | 37.0 us                                                | 36.7 us: 1.01x faster                                 |
| pidigits                 | 198 ms                                                 | 196 ms: 1.01x faster                                  |
| sqlglot_normalize        | 108 ms                                                 | 107 ms: 1.01x faster                                  |
| tomli_loads              | 2.22 sec                                               | 2.21 sec: 1.01x faster                                |
| regex_compile            | 138 ms                                                 | 137 ms: 1.01x faster                                  |
| sqlglot_optimize         | 53.1 ms                                                | 52.9 ms: 1.00x faster                                 |
| pprint_pformat           | 1.46 sec                                               | 1.46 sec: 1.00x slower                                |
| unpickle_list            | 4.91 us                                                | 4.94 us: 1.01x slower                                 |
| bench_thread_pool        | 819 us                                                 | 825 us: 1.01x slower                                  |
| create_gc_cycles         | 1.49 ms                                                | 1.50 ms: 1.01x slower                                 |
| fannkuch                 | 388 ms                                                 | 394 ms: 1.01x slower                                  |
| deepcopy                 | 342 us                                                 | 347 us: 1.02x slower                                  |
| dulwich_log              | 63.7 ms                                                | 65.0 ms: 1.02x slower                                 |
| docutils                 | 2.63 sec                                               | 2.68 sec: 1.02x slower                                |
| pathlib                  | 18.2 ms                                                | 18.7 ms: 1.02x slower                                 |
| pprint_safe_repr         | 701 ms                                                 | 720 ms: 1.03x slower                                  |
| unpack_sequence          | 43.1 ns                                                | 44.3 ns: 1.03x slower                                 |
| spectral_norm            | 100 ms                                                 | 103 ms: 1.03x slower                                  |
| float                    | 77.2 ms                                                | 79.7 ms: 1.03x slower                                 |
| mako                     | 10.1 ms                                                | 10.5 ms: 1.04x slower                                 |
| regex_v8                 | 22.0 ms                                                | 23.0 ms: 1.04x slower                                 |
| crypto_pyaes             | 74.7 ms                                                | 78.2 ms: 1.05x slower                                 |
| scimark_monte_carlo      | 68.1 ms                                                | 71.2 ms: 1.05x slower                                 |
| scimark_sparse_mat_mult  | 4.50 ms                                                | 4.72 ms: 1.05x slower                                 |
| telco                    | 6.58 ms                                                | 6.92 ms: 1.05x slower                                 |
| regex_dna                | 204 ms                                                 | 215 ms: 1.05x slower                                  |
| pyflate                  | 418 ms                                                 | 444 ms: 1.06x slower                                  |
| xml_etree_process        | 53.9 ms                                                | 57.4 ms: 1.07x slower                                 |
| pickle                   | 10.1 us                                                | 10.8 us: 1.07x slower                                 |
| deepcopy_reduce          | 2.94 us                                                | 3.16 us: 1.08x slower                                 |
| python_startup           | 8.52 ms                                                | 9.19 ms: 1.08x slower                                 |
| scimark_fft              | 328 ms                                                 | 357 ms: 1.09x slower                                  |
| sqlite_synth             | 2.52 us                                                | 2.74 us: 1.09x slower                                 |
| xml_etree_generate       | 76.2 ms                                                | 83.8 ms: 1.10x slower                                 |
| pickle_list              | 4.11 us                                                | 4.55 us: 1.11x slower                                 |
| python_startup_no_site   | 6.01 ms                                                | 6.68 ms: 1.11x slower                                 |
| unpickle                 | 13.7 us                                                | 15.3 us: 1.12x slower                                 |
| async_generators         | 368 ms                                                 | 448 ms: 1.22x slower                                  |
| dask                     | 360 ms                                                 | 519 ms: 1.44x slower                                  |
| Geometric mean           | (ref)                                                  | 1.04x faster                                          |

Benchmark hidden because not significant (6): nbody, pickle_pure_python, scimark_sor, bench_mp_pool, tornado_http, pickle_dict
Ignored benchmarks (18) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
