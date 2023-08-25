
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 3eb12df
- commit date: 2023-02-11
- overall geometric mean: 1.04x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230211-linux-x86_64-python-main-3.12.0a5+-3eb12df |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 250 ms: 1.03x faster                                   |
| chameleon      | 6.47 ms                                                | 6.58 ms: 1.02x slower                                  |
| docutils       | 2.63 sec                                               | 2.52 sec: 1.04x faster                                 |
| html5lib       | 64.5 ms                                                | 61.1 ms: 1.06x faster                                  |
| tornado_http   | 96.3 ms                                                | 94.5 ms: 1.02x faster                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230211-linux-x86_64-python-main-3.12.0a5+-3eb12df |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| float          | 77.2 ms                                                | 72.1 ms: 1.07x faster                                  |
| pidigits       | 198 ms                                                 | 193 ms: 1.03x faster                                   |
| nbody          | 93.1 ms                                                | 94.8 ms: 1.02x slower                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230211-linux-x86_64-python-main-3.12.0a5+-3eb12df |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.56 ms: 1.12x faster                                  |
| regex_compile  | 138 ms                                                 | 129 ms: 1.07x faster                                   |
| regex_v8       | 22.0 ms                                                | 21.2 ms: 1.04x faster                                  |
| regex_dna      | 204 ms                                                 | 199 ms: 1.02x faster                                   |
| Geometric mean | (ref)                                                  | 1.06x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230211-linux-x86_64-python-main-3.12.0a5+-3eb12df |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.51 ms: 1.32x faster                                  |
| unpickle_pure_python | 228 us                                                 | 196 us: 1.16x faster                                   |
| json_loads           | 26.5 us                                                | 24.0 us: 1.10x faster                                  |
| xml_etree_parse      | 158 ms                                                 | 148 ms: 1.07x faster                                   |
| pickle_pure_python   | 306 us                                                 | 288 us: 1.06x faster                                   |
| xml_etree_iterparse  | 104 ms                                                 | 102 ms: 1.02x faster                                   |
| pickle_list          | 4.11 us                                                | 4.05 us: 1.02x faster                                  |
| pickle_dict          | 31.1 us                                                | 30.8 us: 1.01x faster                                  |
| unpickle_list        | 4.91 us                                                | 4.95 us: 1.01x slower                                  |
| xml_etree_process    | 53.9 ms                                                | 55.2 ms: 1.02x slower                                  |
| xml_etree_generate   | 76.2 ms                                                | 80.5 ms: 1.06x slower                                  |
| Geometric mean       | (ref)                                                  | 1.05x faster                                           |

Benchmark hidden because not significant (2): unpickle, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230211-linux-x86_64-python-main-3.12.0a5+-3eb12df |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.92 ms: 1.05x slower                                  |
| python_startup_no_site | 6.01 ms                                                | 6.47 ms: 1.08x slower                                  |
| Geometric mean         | (ref)                                                  | 1.06x slower                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230211-linux-x86_64-python-main-3.12.0a5+-3eb12df |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 46.6 ms: 1.11x faster                                  |
| genshi_text     | 21.6 ms                                                | 20.6 ms: 1.05x faster                                  |
| mako            | 10.1 ms                                                | 9.95 ms: 1.01x faster                                  |
| django_template | 32.6 ms                                                | 33.3 ms: 1.02x slower                                  |
| Geometric mean  | (ref)                                                  | 1.04x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230211-linux-x86_64-python-main-3.12.0a5+-3eb12df |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| asyncio_tcp             | 922 ms                                                 | 498 ms: 1.85x faster                                   |
| json_dumps              | 12.6 ms                                                | 9.51 ms: 1.32x faster                                  |
| mypy2                   | 420 ms                                                 | 331 ms: 1.27x faster                                   |
| deltablue               | 3.67 ms                                                | 3.11 ms: 1.18x faster                                  |
| unpickle_pure_python    | 228 us                                                 | 196 us: 1.16x faster                                   |
| regex_effbot            | 3.99 ms                                                | 3.56 ms: 1.12x faster                                  |
| logging_silent          | 101 ns                                                 | 91.0 ns: 1.11x faster                                  |
| genshi_xml              | 51.8 ms                                                | 46.6 ms: 1.11x faster                                  |
| scimark_sor             | 118 ms                                                 | 106 ms: 1.11x faster                                   |
| json_loads              | 26.5 us                                                | 24.0 us: 1.10x faster                                  |
| aiohttp                 | 1.10 ms                                                | 1.01 ms: 1.09x faster                                  |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.13 ms: 1.09x faster                                  |
| gunicorn                | 1.18 ms                                                | 1.09 ms: 1.08x faster                                  |
| richards                | 45.7 ms                                                | 42.3 ms: 1.08x faster                                  |
| hexiom                  | 6.37 ms                                                | 5.91 ms: 1.08x faster                                  |
| deepcopy_memo           | 37.0 us                                                | 34.3 us: 1.08x faster                                  |
| pycparser               | 1.18 sec                                               | 1.10 sec: 1.08x faster                                 |
| nqueens                 | 83.4 ms                                                | 77.6 ms: 1.07x faster                                  |
| regex_compile           | 138 ms                                                 | 129 ms: 1.07x faster                                   |
| float                   | 77.2 ms                                                | 72.1 ms: 1.07x faster                                  |
| fannkuch                | 388 ms                                                 | 363 ms: 1.07x faster                                   |
| json                    | 4.94 ms                                                | 4.63 ms: 1.07x faster                                  |
| xml_etree_parse         | 158 ms                                                 | 148 ms: 1.07x faster                                   |
| sympy_str               | 290 ms                                                 | 273 ms: 1.06x faster                                   |
| pickle_pure_python      | 306 us                                                 | 288 us: 1.06x faster                                   |
| mdp                     | 2.62 sec                                               | 2.47 sec: 1.06x faster                                 |
| html5lib                | 64.5 ms                                                | 61.1 ms: 1.06x faster                                  |
| sympy_integrate         | 21.0 ms                                                | 19.9 ms: 1.06x faster                                  |
| raytrace                | 297 ms                                                 | 281 ms: 1.06x faster                                   |
| scimark_fft             | 328 ms                                                 | 312 ms: 1.05x faster                                   |
| pyflate                 | 418 ms                                                 | 398 ms: 1.05x faster                                   |
| go                      | 140 ms                                                 | 133 ms: 1.05x faster                                   |
| genshi_text             | 21.6 ms                                                | 20.6 ms: 1.05x faster                                  |
| sympy_sum               | 167 ms                                                 | 159 ms: 1.05x faster                                   |
| sqlglot_optimize        | 53.1 ms                                                | 50.8 ms: 1.05x faster                                  |
| docutils                | 2.63 sec                                               | 2.52 sec: 1.04x faster                                 |
| regex_v8                | 22.0 ms                                                | 21.2 ms: 1.04x faster                                  |
| bench_thread_pool       | 819 us                                                 | 786 us: 1.04x faster                                   |
| chaos                   | 69.2 ms                                                | 66.5 ms: 1.04x faster                                  |
| logging_format          | 6.68 us                                                | 6.43 us: 1.04x faster                                  |
| deepcopy                | 342 us                                                 | 329 us: 1.04x faster                                   |
| pprint_pformat          | 1.46 sec                                               | 1.40 sec: 1.04x faster                                 |
| telco                   | 6.58 ms                                                | 6.34 ms: 1.04x faster                                  |
| 2to3                    | 259 ms                                                 | 250 ms: 1.03x faster                                   |
| scimark_monte_carlo     | 68.1 ms                                                | 65.8 ms: 1.03x faster                                  |
| sympy_expand            | 475 ms                                                 | 459 ms: 1.03x faster                                   |
| coverage                | 100 ms                                                 | 96.8 ms: 1.03x faster                                  |
| sqlglot_normalize       | 108 ms                                                 | 104 ms: 1.03x faster                                   |
| pathlib                 | 18.2 ms                                                | 17.7 ms: 1.03x faster                                  |
| pidigits                | 198 ms                                                 | 193 ms: 1.03x faster                                   |
| logging_simple          | 6.03 us                                                | 5.87 us: 1.03x faster                                  |
| create_gc_cycles        | 1.49 ms                                                | 1.45 ms: 1.03x faster                                  |
| pprint_safe_repr        | 701 ms                                                 | 684 ms: 1.03x faster                                   |
| regex_dna               | 204 ms                                                 | 199 ms: 1.02x faster                                   |
| meteor_contest          | 107 ms                                                 | 105 ms: 1.02x faster                                   |
| tornado_http            | 96.3 ms                                                | 94.5 ms: 1.02x faster                                  |
| xml_etree_iterparse     | 104 ms                                                 | 102 ms: 1.02x faster                                   |
| pickle_list             | 4.11 us                                                | 4.05 us: 1.02x faster                                  |
| spectral_norm           | 100 ms                                                 | 98.5 ms: 1.02x faster                                  |
| scimark_lu              | 110 ms                                                 | 108 ms: 1.02x faster                                   |
| mako                    | 10.1 ms                                                | 9.95 ms: 1.01x faster                                  |
| sqlalchemy_declarative  | 138 ms                                                 | 137 ms: 1.01x faster                                   |
| coroutines              | 25.5 ms                                                | 25.2 ms: 1.01x faster                                  |
| pickle_dict             | 31.1 us                                                | 30.8 us: 1.01x faster                                  |
| dulwich_log             | 63.7 ms                                                | 63.1 ms: 1.01x faster                                  |
| thrift                  | 756 us                                                 | 761 us: 1.01x slower                                   |
| unpickle_list           | 4.91 us                                                | 4.95 us: 1.01x slower                                  |
| crypto_pyaes            | 74.7 ms                                                | 75.6 ms: 1.01x slower                                  |
| deepcopy_reduce         | 2.94 us                                                | 2.97 us: 1.01x slower                                  |
| async_tree_io           | 1.30 sec                                               | 1.31 sec: 1.01x slower                                 |
| sqlglot_parse           | 1.40 ms                                                | 1.42 ms: 1.01x slower                                  |
| chameleon               | 6.47 ms                                                | 6.58 ms: 1.02x slower                                  |
| nbody                   | 93.1 ms                                                | 94.8 ms: 1.02x slower                                  |
| unpack_sequence         | 43.1 ns                                                | 43.9 ns: 1.02x slower                                  |
| django_template         | 32.6 ms                                                | 33.3 ms: 1.02x slower                                  |
| async_tree_cpu_io_mixed | 739 ms                                                 | 755 ms: 1.02x slower                                   |
| xml_etree_process       | 53.9 ms                                                | 55.2 ms: 1.02x slower                                  |
| sqlite_synth            | 2.52 us                                                | 2.59 us: 1.03x slower                                  |
| gc_traversal            | 4.02 ms                                                | 4.16 ms: 1.03x slower                                  |
| python_startup          | 8.52 ms                                                | 8.92 ms: 1.05x slower                                  |
| generators              | 73.5 ms                                                | 77.5 ms: 1.05x slower                                  |
| xml_etree_generate      | 76.2 ms                                                | 80.5 ms: 1.06x slower                                  |
| python_startup_no_site  | 6.01 ms                                                | 6.47 ms: 1.08x slower                                  |
| async_generators        | 368 ms                                                 | 428 ms: 1.16x slower                                   |
| Geometric mean          | (ref)                                                  | 1.04x faster                                           |

Benchmark hidden because not significant (8): unpickle, async_tree_memoization, async_tree_none, djangocms, pickle, bench_mp_pool, sqlglot_transpile, sqlalchemy_imperative
Ignored benchmarks (8) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, comprehensions, dask, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x
