
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 61f1e67
- commit date: 2023-02-18
- overall geometric mean: 1.05x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230218-linux-x86_64-python-main-3.12.0a5+-61f1e67 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 247 ms: 1.05x faster                                   |
| docutils       | 2.63 sec                                               | 2.54 sec: 1.04x faster                                 |
| html5lib       | 64.5 ms                                                | 61.1 ms: 1.06x faster                                  |
| tornado_http   | 96.3 ms                                                | 95.2 ms: 1.01x faster                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                           |

Benchmark hidden because not significant (1): chameleon

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230218-linux-x86_64-python-main-3.12.0a5+-61f1e67 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| float          | 77.2 ms                                                | 73.1 ms: 1.06x faster                                  |
| pidigits       | 198 ms                                                 | 189 ms: 1.05x faster                                   |
| Geometric mean | (ref)                                                  | 1.03x faster                                           |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230218-linux-x86_64-python-main-3.12.0a5+-61f1e67 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.38 ms: 1.18x faster                                  |
| regex_compile  | 138 ms                                                 | 130 ms: 1.06x faster                                   |
| regex_dna      | 204 ms                                                 | 220 ms: 1.08x slower                                   |
| Geometric mean | (ref)                                                  | 1.04x faster                                           |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230218-linux-x86_64-python-main-3.12.0a5+-61f1e67 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.58 ms: 1.31x faster                                  |
| unpickle_pure_python | 228 us                                                 | 198 us: 1.15x faster                                   |
| json_loads           | 26.5 us                                                | 23.7 us: 1.12x faster                                  |
| pickle_pure_python   | 306 us                                                 | 283 us: 1.08x faster                                   |
| xml_etree_parse      | 158 ms                                                 | 149 ms: 1.07x faster                                   |
| xml_etree_iterparse  | 104 ms                                                 | 100 ms: 1.04x faster                                   |
| xml_etree_process    | 53.9 ms                                                | 55.4 ms: 1.03x slower                                  |
| unpickle_list        | 4.91 us                                                | 5.06 us: 1.03x slower                                  |
| pickle_list          | 4.11 us                                                | 4.29 us: 1.04x slower                                  |
| pickle_dict          | 31.1 us                                                | 32.5 us: 1.05x slower                                  |
| xml_etree_generate   | 76.2 ms                                                | 81.2 ms: 1.07x slower                                  |
| Geometric mean       | (ref)                                                  | 1.04x faster                                           |

Benchmark hidden because not significant (2): unpickle, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230218-linux-x86_64-python-main-3.12.0a5+-61f1e67 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.00 ms: 1.06x slower                                  |
| python_startup_no_site | 6.01 ms                                                | 6.52 ms: 1.08x slower                                  |
| Geometric mean         | (ref)                                                  | 1.07x slower                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230218-linux-x86_64-python-main-3.12.0a5+-61f1e67 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 48.3 ms: 1.07x faster                                  |
| genshi_text     | 21.6 ms                                                | 21.0 ms: 1.03x faster                                  |
| mako            | 10.1 ms                                                | 9.92 ms: 1.02x faster                                  |
| django_template | 32.6 ms                                                | 34.0 ms: 1.04x slower                                  |
| Geometric mean  | (ref)                                                  | 1.02x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230218-linux-x86_64-python-main-3.12.0a5+-61f1e67 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| generators              | 73.5 ms                                                | 30.5 ms: 2.41x faster                                  |
| asyncio_tcp             | 922 ms                                                 | 501 ms: 1.84x faster                                   |
| json_dumps              | 12.6 ms                                                | 9.58 ms: 1.31x faster                                  |
| mypy2                   | 420 ms                                                 | 331 ms: 1.27x faster                                   |
| regex_effbot            | 3.99 ms                                                | 3.38 ms: 1.18x faster                                  |
| unpickle_pure_python    | 228 us                                                 | 198 us: 1.15x faster                                   |
| deltablue               | 3.67 ms                                                | 3.21 ms: 1.15x faster                                  |
| scimark_sparse_mat_mult | 4.50 ms                                                | 3.98 ms: 1.13x faster                                  |
| json_loads              | 26.5 us                                                | 23.7 us: 1.12x faster                                  |
| coroutines              | 25.5 ms                                                | 22.9 ms: 1.11x faster                                  |
| aiohttp                 | 1.10 ms                                                | 1.01 ms: 1.09x faster                                  |
| json                    | 4.94 ms                                                | 4.54 ms: 1.09x faster                                  |
| richards                | 45.7 ms                                                | 42.0 ms: 1.09x faster                                  |
| scimark_sor             | 118 ms                                                 | 109 ms: 1.09x faster                                   |
| pickle_pure_python      | 306 us                                                 | 283 us: 1.08x faster                                   |
| fannkuch                | 388 ms                                                 | 360 ms: 1.08x faster                                   |
| logging_silent          | 101 ns                                                 | 93.9 ns: 1.08x faster                                  |
| gunicorn                | 1.18 ms                                                | 1.09 ms: 1.08x faster                                  |
| scimark_fft             | 328 ms                                                 | 305 ms: 1.07x faster                                   |
| genshi_xml              | 51.8 ms                                                | 48.3 ms: 1.07x faster                                  |
| xml_etree_parse         | 158 ms                                                 | 149 ms: 1.07x faster                                   |
| sympy_str               | 290 ms                                                 | 273 ms: 1.06x faster                                   |
| regex_compile           | 138 ms                                                 | 130 ms: 1.06x faster                                   |
| deepcopy_memo           | 37.0 us                                                | 34.9 us: 1.06x faster                                  |
| float                   | 77.2 ms                                                | 73.1 ms: 1.06x faster                                  |
| mdp                     | 2.62 sec                                               | 2.48 sec: 1.06x faster                                 |
| html5lib                | 64.5 ms                                                | 61.1 ms: 1.06x faster                                  |
| go                      | 140 ms                                                 | 133 ms: 1.06x faster                                   |
| pycparser               | 1.18 sec                                               | 1.12 sec: 1.06x faster                                 |
| chaos                   | 69.2 ms                                                | 65.7 ms: 1.05x faster                                  |
| sympy_integrate         | 21.0 ms                                                | 19.9 ms: 1.05x faster                                  |
| gc_traversal            | 4.02 ms                                                | 3.83 ms: 1.05x faster                                  |
| 2to3                    | 259 ms                                                 | 247 ms: 1.05x faster                                   |
| sympy_sum               | 167 ms                                                 | 159 ms: 1.05x faster                                   |
| pyflate                 | 418 ms                                                 | 400 ms: 1.05x faster                                   |
| sympy_expand            | 475 ms                                                 | 454 ms: 1.05x faster                                   |
| pidigits                | 198 ms                                                 | 189 ms: 1.05x faster                                   |
| nqueens                 | 83.4 ms                                                | 80.0 ms: 1.04x faster                                  |
| pprint_pformat          | 1.46 sec                                               | 1.40 sec: 1.04x faster                                 |
| sqlglot_optimize        | 53.1 ms                                                | 51.0 ms: 1.04x faster                                  |
| meteor_contest          | 107 ms                                                 | 102 ms: 1.04x faster                                   |
| logging_simple          | 6.03 us                                                | 5.80 us: 1.04x faster                                  |
| coverage                | 100 ms                                                 | 96.3 ms: 1.04x faster                                  |
| raytrace                | 297 ms                                                 | 285 ms: 1.04x faster                                   |
| hexiom                  | 6.37 ms                                                | 6.13 ms: 1.04x faster                                  |
| xml_etree_iterparse     | 104 ms                                                 | 100 ms: 1.04x faster                                   |
| bench_thread_pool       | 819 us                                                 | 790 us: 1.04x faster                                   |
| docutils                | 2.63 sec                                               | 2.54 sec: 1.04x faster                                 |
| spectral_norm           | 100 ms                                                 | 96.6 ms: 1.04x faster                                  |
| sqlglot_normalize       | 108 ms                                                 | 104 ms: 1.03x faster                                   |
| logging_format          | 6.68 us                                                | 6.47 us: 1.03x faster                                  |
| deepcopy                | 342 us                                                 | 332 us: 1.03x faster                                   |
| pprint_safe_repr        | 701 ms                                                 | 682 ms: 1.03x faster                                   |
| genshi_text             | 21.6 ms                                                | 21.0 ms: 1.03x faster                                  |
| scimark_lu              | 110 ms                                                 | 107 ms: 1.03x faster                                   |
| scimark_monte_carlo     | 68.1 ms                                                | 66.4 ms: 1.02x faster                                  |
| crypto_pyaes            | 74.7 ms                                                | 73.2 ms: 1.02x faster                                  |
| telco                   | 6.58 ms                                                | 6.46 ms: 1.02x faster                                  |
| mako                    | 10.1 ms                                                | 9.92 ms: 1.02x faster                                  |
| tornado_http            | 96.3 ms                                                | 95.2 ms: 1.01x faster                                  |
| dulwich_log             | 63.7 ms                                                | 62.9 ms: 1.01x faster                                  |
| unpack_sequence         | 43.1 ns                                                | 42.7 ns: 1.01x faster                                  |
| pathlib                 | 18.2 ms                                                | 18.3 ms: 1.01x slower                                  |
| deepcopy_reduce         | 2.94 us                                                | 2.96 us: 1.01x slower                                  |
| create_gc_cycles        | 1.49 ms                                                | 1.50 ms: 1.01x slower                                  |
| thrift                  | 756 us                                                 | 766 us: 1.01x slower                                   |
| async_tree_cpu_io_mixed | 739 ms                                                 | 749 ms: 1.01x slower                                   |
| sqlglot_transpile       | 1.70 ms                                                | 1.73 ms: 1.02x slower                                  |
| async_tree_io           | 1.30 sec                                               | 1.32 sec: 1.02x slower                                 |
| sqlite_synth            | 2.52 us                                                | 2.59 us: 1.03x slower                                  |
| xml_etree_process       | 53.9 ms                                                | 55.4 ms: 1.03x slower                                  |
| sqlglot_parse           | 1.40 ms                                                | 1.44 ms: 1.03x slower                                  |
| unpickle_list           | 4.91 us                                                | 5.06 us: 1.03x slower                                  |
| async_tree_memoization  | 627 ms                                                 | 649 ms: 1.03x slower                                   |
| django_template         | 32.6 ms                                                | 34.0 ms: 1.04x slower                                  |
| pickle_list             | 4.11 us                                                | 4.29 us: 1.04x slower                                  |
| pickle_dict             | 31.1 us                                                | 32.5 us: 1.05x slower                                  |
| python_startup          | 8.52 ms                                                | 9.00 ms: 1.06x slower                                  |
| xml_etree_generate      | 76.2 ms                                                | 81.2 ms: 1.07x slower                                  |
| regex_dna               | 204 ms                                                 | 220 ms: 1.08x slower                                   |
| python_startup_no_site  | 6.01 ms                                                | 6.52 ms: 1.08x slower                                  |
| async_generators        | 368 ms                                                 | 411 ms: 1.11x slower                                   |
| dask                    | 360 ms                                                 | 501 ms: 1.39x slower                                   |
| Geometric mean          | (ref)                                                  | 1.05x faster                                           |

Benchmark hidden because not significant (10): unpickle, sqlalchemy_declarative, nbody, regex_v8, djangocms, bench_mp_pool, async_tree_none, chameleon, pickle, sqlalchemy_imperative
Ignored benchmarks (7) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, comprehensions, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x
