
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 30a306c
- commit date: 2023-03-25
- overall geometric mean: 1.04x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230325-linux-x86_64-python-main-3.12.0a6+-30a306c |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 254 ms: 1.02x faster                                   |
| chameleon      | 6.47 ms                                                | 6.54 ms: 1.01x slower                                  |
| docutils       | 2.63 sec                                               | 2.56 sec: 1.03x faster                                 |
| html5lib       | 64.5 ms                                                | 62.0 ms: 1.04x faster                                  |
| tornado_http   | 96.3 ms                                                | 91.2 ms: 1.06x faster                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230325-linux-x86_64-python-main-3.12.0a6+-30a306c |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pidigits       | 198 ms                                                 | 188 ms: 1.05x faster                                   |
| float          | 77.2 ms                                                | 73.8 ms: 1.05x faster                                  |
| nbody          | 93.1 ms                                                | 89.5 ms: 1.04x faster                                  |
| Geometric mean | (ref)                                                  | 1.05x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230325-linux-x86_64-python-main-3.12.0a6+-30a306c |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.45 ms: 1.16x faster                                  |
| regex_compile  | 138 ms                                                 | 134 ms: 1.03x faster                                   |
| regex_v8       | 22.0 ms                                                | 22.4 ms: 1.02x slower                                  |
| Geometric mean | (ref)                                                  | 1.04x faster                                           |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230325-linux-x86_64-python-main-3.12.0a6+-30a306c |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.58 ms: 1.31x faster                                  |
| unpickle_pure_python | 228 us                                                 | 200 us: 1.14x faster                                   |
| json_loads           | 26.5 us                                                | 24.0 us: 1.10x faster                                  |
| xml_etree_parse      | 158 ms                                                 | 148 ms: 1.07x faster                                   |
| pickle_pure_python   | 306 us                                                 | 287 us: 1.06x faster                                   |
| unpickle             | 13.7 us                                                | 13.2 us: 1.03x faster                                  |
| xml_etree_iterparse  | 104 ms                                                 | 101 ms: 1.03x faster                                   |
| unpickle_list        | 4.91 us                                                | 4.96 us: 1.01x slower                                  |
| pickle               | 10.1 us                                                | 10.4 us: 1.04x slower                                  |
| pickle_dict          | 31.1 us                                                | 32.3 us: 1.04x slower                                  |
| xml_etree_process    | 53.9 ms                                                | 56.0 ms: 1.04x slower                                  |
| pickle_list          | 4.11 us                                                | 4.35 us: 1.06x slower                                  |
| xml_etree_generate   | 76.2 ms                                                | 81.7 ms: 1.07x slower                                  |
| Geometric mean       | (ref)                                                  | 1.04x faster                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230325-linux-x86_64-python-main-3.12.0a6+-30a306c |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.86 ms: 1.04x slower                                  |
| python_startup_no_site | 6.01 ms                                                | 6.54 ms: 1.09x slower                                  |
| Geometric mean         | (ref)                                                  | 1.06x slower                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230325-linux-x86_64-python-main-3.12.0a6+-30a306c |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 48.3 ms: 1.07x faster                                  |
| mako            | 10.1 ms                                                | 9.82 ms: 1.03x faster                                  |
| genshi_text     | 21.6 ms                                                | 21.3 ms: 1.01x faster                                  |
| django_template | 32.6 ms                                                | 33.5 ms: 1.03x slower                                  |
| Geometric mean  | (ref)                                                  | 1.02x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230325-linux-x86_64-python-main-3.12.0a6+-30a306c |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| generators              | 73.5 ms                                                | 29.6 ms: 2.48x faster                                  |
| asyncio_tcp             | 922 ms                                                 | 504 ms: 1.83x faster                                   |
| json_dumps              | 12.6 ms                                                | 9.58 ms: 1.31x faster                                  |
| mypy2                   | 420 ms                                                 | 333 ms: 1.26x faster                                   |
| regex_effbot            | 3.99 ms                                                | 3.45 ms: 1.16x faster                                  |
| deltablue               | 3.67 ms                                                | 3.21 ms: 1.14x faster                                  |
| unpickle_pure_python    | 228 us                                                 | 200 us: 1.14x faster                                   |
| coroutines              | 25.5 ms                                                | 23.0 ms: 1.11x faster                                  |
| json_loads              | 26.5 us                                                | 24.0 us: 1.10x faster                                  |
| spectral_norm           | 100 ms                                                 | 90.9 ms: 1.10x faster                                  |
| aiohttp                 | 1.10 ms                                                | 1.01 ms: 1.09x faster                                  |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.14 ms: 1.09x faster                                  |
| deepcopy_memo           | 37.0 us                                                | 34.1 us: 1.09x faster                                  |
| gunicorn                | 1.18 ms                                                | 1.09 ms: 1.08x faster                                  |
| json                    | 4.94 ms                                                | 4.59 ms: 1.08x faster                                  |
| scimark_fft             | 328 ms                                                 | 305 ms: 1.08x faster                                   |
| genshi_xml              | 51.8 ms                                                | 48.3 ms: 1.07x faster                                  |
| xml_etree_parse         | 158 ms                                                 | 148 ms: 1.07x faster                                   |
| pickle_pure_python      | 306 us                                                 | 287 us: 1.06x faster                                   |
| hexiom                  | 6.37 ms                                                | 5.99 ms: 1.06x faster                                  |
| logging_format          | 6.68 us                                                | 6.32 us: 1.06x faster                                  |
| tornado_http            | 96.3 ms                                                | 91.2 ms: 1.06x faster                                  |
| scimark_sor             | 118 ms                                                 | 112 ms: 1.05x faster                                   |
| pidigits                | 198 ms                                                 | 188 ms: 1.05x faster                                   |
| chaos                   | 69.2 ms                                                | 65.8 ms: 1.05x faster                                  |
| logging_simple          | 6.03 us                                                | 5.74 us: 1.05x faster                                  |
| raytrace                | 297 ms                                                 | 282 ms: 1.05x faster                                   |
| float                   | 77.2 ms                                                | 73.8 ms: 1.05x faster                                  |
| deepcopy                | 342 us                                                 | 328 us: 1.04x faster                                   |
| html5lib                | 64.5 ms                                                | 62.0 ms: 1.04x faster                                  |
| nbody                   | 93.1 ms                                                | 89.5 ms: 1.04x faster                                  |
| richards                | 45.7 ms                                                | 44.0 ms: 1.04x faster                                  |
| bench_thread_pool       | 819 us                                                 | 790 us: 1.04x faster                                   |
| logging_silent          | 101 ns                                                 | 97.6 ns: 1.04x faster                                  |
| sqlglot_optimize        | 53.1 ms                                                | 51.3 ms: 1.04x faster                                  |
| meteor_contest          | 107 ms                                                 | 103 ms: 1.04x faster                                   |
| unpickle                | 13.7 us                                                | 13.2 us: 1.03x faster                                  |
| fannkuch                | 388 ms                                                 | 375 ms: 1.03x faster                                   |
| scimark_monte_carlo     | 68.1 ms                                                | 65.9 ms: 1.03x faster                                  |
| xml_etree_iterparse     | 104 ms                                                 | 101 ms: 1.03x faster                                   |
| regex_compile           | 138 ms                                                 | 134 ms: 1.03x faster                                   |
| mako                    | 10.1 ms                                                | 9.82 ms: 1.03x faster                                  |
| mdp                     | 2.62 sec                                               | 2.55 sec: 1.03x faster                                 |
| docutils                | 2.63 sec                                               | 2.56 sec: 1.03x faster                                 |
| sympy_expand            | 475 ms                                                 | 463 ms: 1.03x faster                                   |
| coverage                | 100 ms                                                 | 97.6 ms: 1.03x faster                                  |
| go                      | 140 ms                                                 | 137 ms: 1.02x faster                                   |
| gc_traversal            | 4.02 ms                                                | 3.93 ms: 1.02x faster                                  |
| pprint_pformat          | 1.46 sec                                               | 1.42 sec: 1.02x faster                                 |
| sympy_integrate         | 21.0 ms                                                | 20.5 ms: 1.02x faster                                  |
| unpack_sequence         | 43.1 ns                                                | 42.1 ns: 1.02x faster                                  |
| telco                   | 6.58 ms                                                | 6.44 ms: 1.02x faster                                  |
| pyflate                 | 418 ms                                                 | 410 ms: 1.02x faster                                   |
| crypto_pyaes            | 74.7 ms                                                | 73.2 ms: 1.02x faster                                  |
| 2to3                    | 259 ms                                                 | 254 ms: 1.02x faster                                   |
| sympy_str               | 290 ms                                                 | 285 ms: 1.02x faster                                   |
| sqlglot_normalize       | 108 ms                                                 | 106 ms: 1.02x faster                                   |
| pathlib                 | 18.2 ms                                                | 17.9 ms: 1.02x faster                                  |
| pprint_safe_repr        | 701 ms                                                 | 692 ms: 1.01x faster                                   |
| genshi_text             | 21.6 ms                                                | 21.3 ms: 1.01x faster                                  |
| async_tree_none         | 526 ms                                                 | 520 ms: 1.01x faster                                   |
| nqueens                 | 83.4 ms                                                | 82.5 ms: 1.01x faster                                  |
| sqlglot_transpile       | 1.70 ms                                                | 1.72 ms: 1.01x slower                                  |
| chameleon               | 6.47 ms                                                | 6.54 ms: 1.01x slower                                  |
| unpickle_list           | 4.91 us                                                | 4.96 us: 1.01x slower                                  |
| sqlglot_parse           | 1.40 ms                                                | 1.42 ms: 1.02x slower                                  |
| regex_v8                | 22.0 ms                                                | 22.4 ms: 1.02x slower                                  |
| deepcopy_reduce         | 2.94 us                                                | 3.00 us: 1.02x slower                                  |
| async_tree_memoization  | 627 ms                                                 | 643 ms: 1.02x slower                                   |
| django_template         | 32.6 ms                                                | 33.5 ms: 1.03x slower                                  |
| pickle                  | 10.1 us                                                | 10.4 us: 1.04x slower                                  |
| pickle_dict             | 31.1 us                                                | 32.3 us: 1.04x slower                                  |
| python_startup          | 8.52 ms                                                | 8.86 ms: 1.04x slower                                  |
| xml_etree_process       | 53.9 ms                                                | 56.0 ms: 1.04x slower                                  |
| comprehensions          | 22.4 us                                                | 23.5 us: 1.05x slower                                  |
| sqlite_synth            | 2.52 us                                                | 2.65 us: 1.05x slower                                  |
| thrift                  | 756 us                                                 | 795 us: 1.05x slower                                   |
| pickle_list             | 4.11 us                                                | 4.35 us: 1.06x slower                                  |
| xml_etree_generate      | 76.2 ms                                                | 81.7 ms: 1.07x slower                                  |
| python_startup_no_site  | 6.01 ms                                                | 6.54 ms: 1.09x slower                                  |
| async_generators        | 368 ms                                                 | 409 ms: 1.11x slower                                   |
| dask                    | 360 ms                                                 | 514 ms: 1.43x slower                                   |
| Geometric mean          | (ref)                                                  | 1.04x faster                                           |

Benchmark hidden because not significant (12): djangocms, async_tree_cpu_io_mixed, scimark_lu, sqlalchemy_declarative, pycparser, create_gc_cycles, sympy_sum, regex_dna, async_tree_io, bench_mp_pool, dulwich_log, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x
