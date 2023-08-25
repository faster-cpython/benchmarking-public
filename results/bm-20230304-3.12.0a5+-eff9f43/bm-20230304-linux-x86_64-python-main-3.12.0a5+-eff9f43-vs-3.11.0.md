
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: eff9f43
- commit date: 2023-03-04
- overall geometric mean: 1.03x faster \*
- HPT reliability: 99.99%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230304-linux-x86_64-python-main-3.12.0a5+-eff9f43 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 250 ms: 1.03x faster                                   |
| chameleon      | 6.47 ms                                                | 6.42 ms: 1.01x faster                                  |
| docutils       | 2.63 sec                                               | 2.56 sec: 1.03x faster                                 |
| html5lib       | 64.5 ms                                                | 61.4 ms: 1.05x faster                                  |
| tornado_http   | 96.3 ms                                                | 94.9 ms: 1.01x faster                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230304-linux-x86_64-python-main-3.12.0a5+-eff9f43 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pidigits       | 198 ms                                                 | 190 ms: 1.04x faster                                   |
| float          | 77.2 ms                                                | 74.6 ms: 1.04x faster                                  |
| nbody          | 93.1 ms                                                | 94.0 ms: 1.01x slower                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230304-linux-x86_64-python-main-3.12.0a5+-eff9f43 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.40 ms: 1.18x faster                                  |
| regex_compile  | 138 ms                                                 | 133 ms: 1.04x faster                                   |
| regex_v8       | 22.0 ms                                                | 21.8 ms: 1.01x faster                                  |
| regex_dna      | 204 ms                                                 | 209 ms: 1.02x slower                                   |
| Geometric mean | (ref)                                                  | 1.05x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230304-linux-x86_64-python-main-3.12.0a5+-eff9f43 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.56 ms: 1.32x faster                                  |
| unpickle_pure_python | 228 us                                                 | 199 us: 1.15x faster                                   |
| json_loads           | 26.5 us                                                | 23.9 us: 1.11x faster                                  |
| xml_etree_parse      | 158 ms                                                 | 148 ms: 1.07x faster                                   |
| pickle_pure_python   | 306 us                                                 | 291 us: 1.05x faster                                   |
| xml_etree_iterparse  | 104 ms                                                 | 102 ms: 1.02x faster                                   |
| pickle_list          | 4.11 us                                                | 4.05 us: 1.02x faster                                  |
| pickle               | 10.1 us                                                | 10.2 us: 1.01x slower                                  |
| pickle_dict          | 31.1 us                                                | 31.5 us: 1.01x slower                                  |
| xml_etree_process    | 53.9 ms                                                | 55.4 ms: 1.03x slower                                  |
| unpickle_list        | 4.91 us                                                | 5.22 us: 1.06x slower                                  |
| xml_etree_generate   | 76.2 ms                                                | 81.3 ms: 1.07x slower                                  |
| Geometric mean       | (ref)                                                  | 1.04x faster                                           |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230304-linux-x86_64-python-main-3.12.0a5+-eff9f43 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.03 ms: 1.06x slower                                  |
| python_startup_no_site | 6.01 ms                                                | 6.55 ms: 1.09x slower                                  |
| Geometric mean         | (ref)                                                  | 1.08x slower                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230304-linux-x86_64-python-main-3.12.0a5+-eff9f43 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 48.6 ms: 1.07x faster                                  |
| genshi_text     | 21.6 ms                                                | 21.2 ms: 1.02x faster                                  |
| django_template | 32.6 ms                                                | 33.2 ms: 1.02x slower                                  |
| Geometric mean  | (ref)                                                  | 1.02x faster                                           |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230304-linux-x86_64-python-main-3.12.0a5+-eff9f43 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| generators              | 73.5 ms                                                | 30.6 ms: 2.40x faster                                  |
| asyncio_tcp             | 922 ms                                                 | 508 ms: 1.81x faster                                   |
| json_dumps              | 12.6 ms                                                | 9.56 ms: 1.32x faster                                  |
| mypy2                   | 420 ms                                                 | 334 ms: 1.26x faster                                   |
| regex_effbot            | 3.99 ms                                                | 3.40 ms: 1.18x faster                                  |
| unpickle_pure_python    | 228 us                                                 | 199 us: 1.15x faster                                   |
| deltablue               | 3.67 ms                                                | 3.20 ms: 1.15x faster                                  |
| json_loads              | 26.5 us                                                | 23.9 us: 1.11x faster                                  |
| aiohttp                 | 1.10 ms                                                | 1.01 ms: 1.09x faster                                  |
| scimark_sor             | 118 ms                                                 | 109 ms: 1.09x faster                                   |
| coroutines              | 25.5 ms                                                | 23.5 ms: 1.09x faster                                  |
| logging_silent          | 101 ns                                                 | 93.2 ns: 1.08x faster                                  |
| gunicorn                | 1.18 ms                                                | 1.09 ms: 1.08x faster                                  |
| json                    | 4.94 ms                                                | 4.59 ms: 1.08x faster                                  |
| deepcopy_memo           | 37.0 us                                                | 34.4 us: 1.08x faster                                  |
| richards                | 45.7 ms                                                | 42.6 ms: 1.07x faster                                  |
| pycparser               | 1.18 sec                                               | 1.10 sec: 1.07x faster                                 |
| xml_etree_parse         | 158 ms                                                 | 148 ms: 1.07x faster                                   |
| genshi_xml              | 51.8 ms                                                | 48.6 ms: 1.07x faster                                  |
| go                      | 140 ms                                                 | 133 ms: 1.05x faster                                   |
| mdp                     | 2.62 sec                                               | 2.49 sec: 1.05x faster                                 |
| html5lib                | 64.5 ms                                                | 61.4 ms: 1.05x faster                                  |
| pickle_pure_python      | 306 us                                                 | 291 us: 1.05x faster                                   |
| gc_traversal            | 4.02 ms                                                | 3.84 ms: 1.05x faster                                  |
| fannkuch                | 388 ms                                                 | 371 ms: 1.05x faster                                   |
| pidigits                | 198 ms                                                 | 190 ms: 1.04x faster                                   |
| deepcopy                | 342 us                                                 | 329 us: 1.04x faster                                   |
| regex_compile           | 138 ms                                                 | 133 ms: 1.04x faster                                   |
| pprint_pformat          | 1.46 sec                                               | 1.41 sec: 1.04x faster                                 |
| logging_simple          | 6.03 us                                                | 5.83 us: 1.04x faster                                  |
| float                   | 77.2 ms                                                | 74.6 ms: 1.04x faster                                  |
| sqlglot_optimize        | 53.1 ms                                                | 51.3 ms: 1.03x faster                                  |
| 2to3                    | 259 ms                                                 | 250 ms: 1.03x faster                                   |
| sqlglot_normalize       | 108 ms                                                 | 104 ms: 1.03x faster                                   |
| bench_thread_pool       | 819 us                                                 | 794 us: 1.03x faster                                   |
| logging_format          | 6.68 us                                                | 6.48 us: 1.03x faster                                  |
| hexiom                  | 6.37 ms                                                | 6.18 ms: 1.03x faster                                  |
| docutils                | 2.63 sec                                               | 2.56 sec: 1.03x faster                                 |
| spectral_norm           | 100 ms                                                 | 97.3 ms: 1.03x faster                                  |
| meteor_contest          | 107 ms                                                 | 104 ms: 1.02x faster                                   |
| pprint_safe_repr        | 701 ms                                                 | 687 ms: 1.02x faster                                   |
| scimark_fft             | 328 ms                                                 | 322 ms: 1.02x faster                                   |
| sympy_expand            | 475 ms                                                 | 466 ms: 1.02x faster                                   |
| coverage                | 100 ms                                                 | 98.3 ms: 1.02x faster                                  |
| xml_etree_iterparse     | 104 ms                                                 | 102 ms: 1.02x faster                                   |
| genshi_text             | 21.6 ms                                                | 21.2 ms: 1.02x faster                                  |
| pickle_list             | 4.11 us                                                | 4.05 us: 1.02x faster                                  |
| chaos                   | 69.2 ms                                                | 68.1 ms: 1.02x faster                                  |
| tornado_http            | 96.3 ms                                                | 94.9 ms: 1.01x faster                                  |
| nqueens                 | 83.4 ms                                                | 82.2 ms: 1.01x faster                                  |
| sympy_integrate         | 21.0 ms                                                | 20.7 ms: 1.01x faster                                  |
| pathlib                 | 18.2 ms                                                | 18.0 ms: 1.01x faster                                  |
| regex_v8                | 22.0 ms                                                | 21.8 ms: 1.01x faster                                  |
| chameleon               | 6.47 ms                                                | 6.42 ms: 1.01x faster                                  |
| sympy_str               | 290 ms                                                 | 288 ms: 1.01x faster                                   |
| dulwich_log             | 63.7 ms                                                | 63.2 ms: 1.01x faster                                  |
| crypto_pyaes            | 74.7 ms                                                | 75.2 ms: 1.01x slower                                  |
| nbody                   | 93.1 ms                                                | 94.0 ms: 1.01x slower                                  |
| sympy_sum               | 167 ms                                                 | 168 ms: 1.01x slower                                   |
| pickle                  | 10.1 us                                                | 10.2 us: 1.01x slower                                  |
| pickle_dict             | 31.1 us                                                | 31.5 us: 1.01x slower                                  |
| create_gc_cycles        | 1.49 ms                                                | 1.50 ms: 1.01x slower                                  |
| pyflate                 | 418 ms                                                 | 424 ms: 1.01x slower                                   |
| django_template         | 32.6 ms                                                | 33.2 ms: 1.02x slower                                  |
| sqlglot_transpile       | 1.70 ms                                                | 1.74 ms: 1.02x slower                                  |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.60 ms: 1.02x slower                                  |
| regex_dna               | 204 ms                                                 | 209 ms: 1.02x slower                                   |
| scimark_lu              | 110 ms                                                 | 112 ms: 1.02x slower                                   |
| thrift                  | 756 us                                                 | 777 us: 1.03x slower                                   |
| xml_etree_process       | 53.9 ms                                                | 55.4 ms: 1.03x slower                                  |
| sqlglot_parse           | 1.40 ms                                                | 1.45 ms: 1.03x slower                                  |
| async_tree_memoization  | 627 ms                                                 | 653 ms: 1.04x slower                                   |
| sqlite_synth            | 2.52 us                                                | 2.63 us: 1.05x slower                                  |
| python_startup          | 8.52 ms                                                | 9.03 ms: 1.06x slower                                  |
| unpickle_list           | 4.91 us                                                | 5.22 us: 1.06x slower                                  |
| xml_etree_generate      | 76.2 ms                                                | 81.3 ms: 1.07x slower                                  |
| comprehensions          | 22.4 us                                                | 24.1 us: 1.07x slower                                  |
| python_startup_no_site  | 6.01 ms                                                | 6.55 ms: 1.09x slower                                  |
| async_generators        | 368 ms                                                 | 421 ms: 1.14x slower                                   |
| dask                    | 360 ms                                                 | 507 ms: 1.41x slower                                   |
| Geometric mean          | (ref)                                                  | 1.03x faster                                           |

Benchmark hidden because not significant (14): async_tree_none, scimark_monte_carlo, mako, sqlalchemy_declarative, async_tree_io, bench_mp_pool, deepcopy_reduce, djangocms, unpack_sequence, unpickle, raytrace, telco, sqlalchemy_imperative, async_tree_cpu_io_mixed
Ignored benchmarks (6) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x
