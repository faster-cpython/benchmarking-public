
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: bb396ee
- commit date: 2023-03-11
- overall geometric mean: 1.04x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230311-linux-x86_64-python-main-3.12.0a6+-bb396ee |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 250 ms: 1.03x faster                                   |
| chameleon      | 6.47 ms                                                | 6.37 ms: 1.02x faster                                  |
| docutils       | 2.63 sec                                               | 2.55 sec: 1.03x faster                                 |
| html5lib       | 64.5 ms                                                | 61.6 ms: 1.05x faster                                  |
| tornado_http   | 96.3 ms                                                | 91.2 ms: 1.06x faster                                  |
| Geometric mean | (ref)                                                  | 1.04x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230311-linux-x86_64-python-main-3.12.0a6+-bb396ee |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| float          | 77.2 ms                                                | 74.1 ms: 1.04x faster                                  |
| pidigits       | 198 ms                                                 | 192 ms: 1.03x faster                                   |
| nbody          | 93.1 ms                                                | 92.1 ms: 1.01x faster                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230311-linux-x86_64-python-main-3.12.0a6+-bb396ee |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.66 ms: 1.09x faster                                  |
| regex_compile  | 138 ms                                                 | 134 ms: 1.03x faster                                   |
| regex_v8       | 22.0 ms                                                | 21.7 ms: 1.01x faster                                  |
| regex_dna      | 204 ms                                                 | 205 ms: 1.01x slower                                   |
| Geometric mean | (ref)                                                  | 1.03x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230311-linux-x86_64-python-main-3.12.0a6+-bb396ee |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.48 ms: 1.33x faster                                  |
| unpickle_pure_python | 228 us                                                 | 201 us: 1.13x faster                                   |
| json_loads           | 26.5 us                                                | 24.0 us: 1.10x faster                                  |
| xml_etree_parse      | 158 ms                                                 | 147 ms: 1.08x faster                                   |
| pickle_pure_python   | 306 us                                                 | 287 us: 1.07x faster                                   |
| xml_etree_iterparse  | 104 ms                                                 | 101 ms: 1.03x faster                                   |
| pickle_dict          | 31.1 us                                                | 31.3 us: 1.00x slower                                  |
| unpickle_list        | 4.91 us                                                | 4.98 us: 1.01x slower                                  |
| pickle_list          | 4.11 us                                                | 4.24 us: 1.03x slower                                  |
| xml_etree_process    | 53.9 ms                                                | 55.8 ms: 1.04x slower                                  |
| pickle               | 10.1 us                                                | 10.4 us: 1.04x slower                                  |
| xml_etree_generate   | 76.2 ms                                                | 80.6 ms: 1.06x slower                                  |
| Geometric mean       | (ref)                                                  | 1.04x faster                                           |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230311-linux-x86_64-python-main-3.12.0a6+-bb396ee |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.96 ms: 1.05x slower                                  |
| python_startup_no_site | 6.01 ms                                                | 6.50 ms: 1.08x slower                                  |
| Geometric mean         | (ref)                                                  | 1.07x slower                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230311-linux-x86_64-python-main-3.12.0a6+-bb396ee |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 48.2 ms: 1.07x faster                                  |
| mako            | 10.1 ms                                                | 10.1 ms: 1.01x slower                                  |
| django_template | 32.6 ms                                                | 32.9 ms: 1.01x slower                                  |
| genshi_text     | 21.6 ms                                                | 21.8 ms: 1.01x slower                                  |
| Geometric mean  | (ref)                                                  | 1.01x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230311-linux-x86_64-python-main-3.12.0a6+-bb396ee |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| generators              | 73.5 ms                                                | 30.3 ms: 2.42x faster                                  |
| asyncio_tcp             | 922 ms                                                 | 502 ms: 1.84x faster                                   |
| json_dumps              | 12.6 ms                                                | 9.48 ms: 1.33x faster                                  |
| mypy2                   | 420 ms                                                 | 333 ms: 1.26x faster                                   |
| deltablue               | 3.67 ms                                                | 3.22 ms: 1.14x faster                                  |
| unpickle_pure_python    | 228 us                                                 | 201 us: 1.13x faster                                   |
| coroutines              | 25.5 ms                                                | 22.7 ms: 1.12x faster                                  |
| scimark_sor             | 118 ms                                                 | 107 ms: 1.10x faster                                   |
| json_loads              | 26.5 us                                                | 24.0 us: 1.10x faster                                  |
| gc_traversal            | 4.02 ms                                                | 3.66 ms: 1.10x faster                                  |
| fannkuch                | 388 ms                                                 | 355 ms: 1.09x faster                                   |
| regex_effbot            | 3.99 ms                                                | 3.66 ms: 1.09x faster                                  |
| aiohttp                 | 1.10 ms                                                | 1.01 ms: 1.09x faster                                  |
| gunicorn                | 1.18 ms                                                | 1.09 ms: 1.08x faster                                  |
| json                    | 4.94 ms                                                | 4.57 ms: 1.08x faster                                  |
| xml_etree_parse         | 158 ms                                                 | 147 ms: 1.08x faster                                   |
| genshi_xml              | 51.8 ms                                                | 48.2 ms: 1.07x faster                                  |
| spectral_norm           | 100 ms                                                 | 93.3 ms: 1.07x faster                                  |
| pickle_pure_python      | 306 us                                                 | 287 us: 1.07x faster                                   |
| richards                | 45.7 ms                                                | 42.9 ms: 1.07x faster                                  |
| deepcopy_memo           | 37.0 us                                                | 34.8 us: 1.06x faster                                  |
| logging_silent          | 101 ns                                                 | 95.2 ns: 1.06x faster                                  |
| tornado_http            | 96.3 ms                                                | 91.2 ms: 1.06x faster                                  |
| logging_format          | 6.68 us                                                | 6.36 us: 1.05x faster                                  |
| scimark_fft             | 328 ms                                                 | 313 ms: 1.05x faster                                   |
| html5lib                | 64.5 ms                                                | 61.6 ms: 1.05x faster                                  |
| pprint_pformat          | 1.46 sec                                               | 1.39 sec: 1.05x faster                                 |
| pycparser               | 1.18 sec                                               | 1.13 sec: 1.05x faster                                 |
| logging_simple          | 6.03 us                                                | 5.77 us: 1.05x faster                                  |
| unpack_sequence         | 43.1 ns                                                | 41.3 ns: 1.04x faster                                  |
| raytrace                | 297 ms                                                 | 284 ms: 1.04x faster                                   |
| float                   | 77.2 ms                                                | 74.1 ms: 1.04x faster                                  |
| sqlglot_optimize        | 53.1 ms                                                | 51.0 ms: 1.04x faster                                  |
| pyflate                 | 418 ms                                                 | 403 ms: 1.04x faster                                   |
| bench_thread_pool       | 819 us                                                 | 789 us: 1.04x faster                                   |
| go                      | 140 ms                                                 | 135 ms: 1.04x faster                                   |
| 2to3                    | 259 ms                                                 | 250 ms: 1.03x faster                                   |
| hexiom                  | 6.37 ms                                                | 6.17 ms: 1.03x faster                                  |
| pprint_safe_repr        | 701 ms                                                 | 680 ms: 1.03x faster                                   |
| regex_compile           | 138 ms                                                 | 134 ms: 1.03x faster                                   |
| sympy_expand            | 475 ms                                                 | 461 ms: 1.03x faster                                   |
| pidigits                | 198 ms                                                 | 192 ms: 1.03x faster                                   |
| docutils                | 2.63 sec                                               | 2.55 sec: 1.03x faster                                 |
| pathlib                 | 18.2 ms                                                | 17.7 ms: 1.03x faster                                  |
| coverage                | 100 ms                                                 | 97.3 ms: 1.03x faster                                  |
| xml_etree_iterparse     | 104 ms                                                 | 101 ms: 1.03x faster                                   |
| mdp                     | 2.62 sec                                               | 2.55 sec: 1.03x faster                                 |
| sqlglot_normalize       | 108 ms                                                 | 105 ms: 1.03x faster                                   |
| sympy_integrate         | 21.0 ms                                                | 20.5 ms: 1.02x faster                                  |
| scimark_monte_carlo     | 68.1 ms                                                | 66.5 ms: 1.02x faster                                  |
| create_gc_cycles        | 1.49 ms                                                | 1.45 ms: 1.02x faster                                  |
| sympy_str               | 290 ms                                                 | 284 ms: 1.02x faster                                   |
| chaos                   | 69.2 ms                                                | 67.8 ms: 1.02x faster                                  |
| deepcopy                | 342 us                                                 | 336 us: 1.02x faster                                   |
| chameleon               | 6.47 ms                                                | 6.37 ms: 1.02x faster                                  |
| telco                   | 6.58 ms                                                | 6.49 ms: 1.01x faster                                  |
| regex_v8                | 22.0 ms                                                | 21.7 ms: 1.01x faster                                  |
| sqlalchemy_imperative   | 17.9 ms                                                | 17.7 ms: 1.01x faster                                  |
| async_tree_none         | 526 ms                                                 | 520 ms: 1.01x faster                                   |
| nbody                   | 93.1 ms                                                | 92.1 ms: 1.01x faster                                  |
| async_tree_io           | 1.30 sec                                               | 1.28 sec: 1.01x faster                                 |
| crypto_pyaes            | 74.7 ms                                                | 73.9 ms: 1.01x faster                                  |
| pickle_dict             | 31.1 us                                                | 31.3 us: 1.00x slower                                  |
| mako                    | 10.1 ms                                                | 10.1 ms: 1.01x slower                                  |
| regex_dna               | 204 ms                                                 | 205 ms: 1.01x slower                                   |
| django_template         | 32.6 ms                                                | 32.9 ms: 1.01x slower                                  |
| sqlglot_transpile       | 1.70 ms                                                | 1.72 ms: 1.01x slower                                  |
| genshi_text             | 21.6 ms                                                | 21.8 ms: 1.01x slower                                  |
| sqlalchemy_declarative  | 138 ms                                                 | 140 ms: 1.01x slower                                   |
| unpickle_list           | 4.91 us                                                | 4.98 us: 1.01x slower                                  |
| sqlglot_parse           | 1.40 ms                                                | 1.42 ms: 1.01x slower                                  |
| deepcopy_reduce         | 2.94 us                                                | 3.00 us: 1.02x slower                                  |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.59 ms: 1.02x slower                                  |
| pickle_list             | 4.11 us                                                | 4.24 us: 1.03x slower                                  |
| thrift                  | 756 us                                                 | 782 us: 1.03x slower                                   |
| async_tree_memoization  | 627 ms                                                 | 649 ms: 1.04x slower                                   |
| xml_etree_process       | 53.9 ms                                                | 55.8 ms: 1.04x slower                                  |
| pickle                  | 10.1 us                                                | 10.4 us: 1.04x slower                                  |
| scimark_lu              | 110 ms                                                 | 114 ms: 1.04x slower                                   |
| sqlite_synth            | 2.52 us                                                | 2.63 us: 1.05x slower                                  |
| python_startup          | 8.52 ms                                                | 8.96 ms: 1.05x slower                                  |
| comprehensions          | 22.4 us                                                | 23.7 us: 1.06x slower                                  |
| xml_etree_generate      | 76.2 ms                                                | 80.6 ms: 1.06x slower                                  |
| python_startup_no_site  | 6.01 ms                                                | 6.50 ms: 1.08x slower                                  |
| async_generators        | 368 ms                                                 | 415 ms: 1.13x slower                                   |
| dask                    | 360 ms                                                 | 499 ms: 1.39x slower                                   |
| Geometric mean          | (ref)                                                  | 1.04x faster                                           |

Benchmark hidden because not significant (8): unpickle, meteor_contest, async_tree_cpu_io_mixed, bench_mp_pool, nqueens, dulwich_log, sympy_sum, djangocms
Ignored benchmarks (6) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x
