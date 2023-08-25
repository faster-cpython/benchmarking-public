
# Results vs. 3.11.0

- fork: brandtbucher
- ref: replicate_load_fast
- machine: linux-x86_64
- commit hash: 7dd73c5
- commit date: 2023-02-16
- overall geometric mean: 1.05x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230216-linux-x86_64-brandtbucher-replicate_load_fast-3.12.0a5+-7dd73c5 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 248 ms: 1.05x faster                                                        |
| chameleon      | 6.47 ms                                                | 6.34 ms: 1.02x faster                                                       |
| docutils       | 2.63 sec                                               | 2.57 sec: 1.02x faster                                                      |
| html5lib       | 64.5 ms                                                | 61.8 ms: 1.04x faster                                                       |
| tornado_http   | 96.3 ms                                                | 95.5 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230216-linux-x86_64-brandtbucher-replicate_load_fast-3.12.0a5+-7dd73c5 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 77.2 ms                                                | 72.6 ms: 1.06x faster                                                       |
| pidigits       | 198 ms                                                 | 189 ms: 1.05x faster                                                        |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230216-linux-x86_64-brandtbucher-replicate_load_fast-3.12.0a5+-7dd73c5 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.67 ms: 1.09x faster                                                       |
| regex_compile  | 138 ms                                                 | 132 ms: 1.05x faster                                                        |
| regex_v8       | 22.0 ms                                                | 21.6 ms: 1.02x faster                                                       |
| regex_dna      | 204 ms                                                 | 208 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230216-linux-x86_64-brandtbucher-replicate_load_fast-3.12.0a5+-7dd73c5 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.66 ms: 1.30x faster                                                       |
| unpickle_pure_python | 228 us                                                 | 199 us: 1.14x faster                                                        |
| json_loads           | 26.5 us                                                | 24.1 us: 1.10x faster                                                       |
| pickle_pure_python   | 306 us                                                 | 283 us: 1.08x faster                                                        |
| xml_etree_parse      | 158 ms                                                 | 148 ms: 1.07x faster                                                        |
| xml_etree_iterparse  | 104 ms                                                 | 103 ms: 1.01x faster                                                        |
| pickle_dict          | 31.1 us                                                | 31.8 us: 1.02x slower                                                       |
| pickle_list          | 4.11 us                                                | 4.26 us: 1.04x slower                                                       |
| unpickle_list        | 4.91 us                                                | 5.13 us: 1.05x slower                                                       |
| xml_etree_process    | 53.9 ms                                                | 56.5 ms: 1.05x slower                                                       |
| xml_etree_generate   | 76.2 ms                                                | 82.5 ms: 1.08x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                                |

Benchmark hidden because not significant (2): unpickle, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230216-linux-x86_64-brandtbucher-replicate_load_fast-3.12.0a5+-7dd73c5 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.00 ms: 1.06x slower                                                       |
| python_startup_no_site | 6.01 ms                                                | 6.53 ms: 1.09x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230216-linux-x86_64-brandtbucher-replicate_load_fast-3.12.0a5+-7dd73c5 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 47.4 ms: 1.09x faster                                                       |
| mako            | 10.1 ms                                                | 9.67 ms: 1.04x faster                                                       |
| genshi_text     | 21.6 ms                                                | 21.1 ms: 1.02x faster                                                       |
| django_template | 32.6 ms                                                | 33.1 ms: 1.02x slower                                                       |
| Geometric mean  | (ref)                                                  | 1.04x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230216-linux-x86_64-brandtbucher-replicate_load_fast-3.12.0a5+-7dd73c5 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| generators              | 73.5 ms                                                | 30.6 ms: 2.40x faster                                                       |
| asyncio_tcp             | 922 ms                                                 | 505 ms: 1.83x faster                                                        |
| json_dumps              | 12.6 ms                                                | 9.66 ms: 1.30x faster                                                       |
| mypy2                   | 420 ms                                                 | 335 ms: 1.25x faster                                                        |
| coroutines              | 25.5 ms                                                | 22.2 ms: 1.15x faster                                                       |
| unpickle_pure_python    | 228 us                                                 | 199 us: 1.14x faster                                                        |
| deltablue               | 3.67 ms                                                | 3.22 ms: 1.14x faster                                                       |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.04 ms: 1.11x faster                                                       |
| scimark_sor             | 118 ms                                                 | 107 ms: 1.10x faster                                                        |
| gc_traversal            | 4.02 ms                                                | 3.66 ms: 1.10x faster                                                       |
| json_loads              | 26.5 us                                                | 24.1 us: 1.10x faster                                                       |
| genshi_xml              | 51.8 ms                                                | 47.4 ms: 1.09x faster                                                       |
| aiohttp                 | 1.10 ms                                                | 1.01 ms: 1.09x faster                                                       |
| regex_effbot            | 3.99 ms                                                | 3.67 ms: 1.09x faster                                                       |
| gunicorn                | 1.18 ms                                                | 1.09 ms: 1.08x faster                                                       |
| richards                | 45.7 ms                                                | 42.3 ms: 1.08x faster                                                       |
| json                    | 4.94 ms                                                | 4.58 ms: 1.08x faster                                                       |
| pickle_pure_python      | 306 us                                                 | 283 us: 1.08x faster                                                        |
| logging_silent          | 101 ns                                                 | 94.1 ns: 1.07x faster                                                       |
| pycparser               | 1.18 sec                                               | 1.10 sec: 1.07x faster                                                      |
| xml_etree_parse         | 158 ms                                                 | 148 ms: 1.07x faster                                                        |
| spectral_norm           | 100 ms                                                 | 93.8 ms: 1.07x faster                                                       |
| float                   | 77.2 ms                                                | 72.6 ms: 1.06x faster                                                       |
| logging_format          | 6.68 us                                                | 6.28 us: 1.06x faster                                                       |
| logging_simple          | 6.03 us                                                | 5.69 us: 1.06x faster                                                       |
| deepcopy_memo           | 37.0 us                                                | 35.0 us: 1.06x faster                                                       |
| sympy_str               | 290 ms                                                 | 275 ms: 1.06x faster                                                        |
| fannkuch                | 388 ms                                                 | 368 ms: 1.05x faster                                                        |
| scimark_fft             | 328 ms                                                 | 312 ms: 1.05x faster                                                        |
| mdp                     | 2.62 sec                                               | 2.49 sec: 1.05x faster                                                      |
| sympy_integrate         | 21.0 ms                                                | 20.0 ms: 1.05x faster                                                       |
| coverage                | 100 ms                                                 | 95.3 ms: 1.05x faster                                                       |
| regex_compile           | 138 ms                                                 | 132 ms: 1.05x faster                                                        |
| nqueens                 | 83.4 ms                                                | 79.5 ms: 1.05x faster                                                       |
| 2to3                    | 259 ms                                                 | 248 ms: 1.05x faster                                                        |
| pidigits                | 198 ms                                                 | 189 ms: 1.05x faster                                                        |
| scimark_monte_carlo     | 68.1 ms                                                | 65.2 ms: 1.04x faster                                                       |
| mako                    | 10.1 ms                                                | 9.67 ms: 1.04x faster                                                       |
| html5lib                | 64.5 ms                                                | 61.8 ms: 1.04x faster                                                       |
| sympy_sum               | 167 ms                                                 | 160 ms: 1.04x faster                                                        |
| unpack_sequence         | 43.1 ns                                                | 41.4 ns: 1.04x faster                                                       |
| sqlglot_optimize        | 53.1 ms                                                | 51.2 ms: 1.04x faster                                                       |
| bench_thread_pool       | 819 us                                                 | 792 us: 1.03x faster                                                        |
| meteor_contest          | 107 ms                                                 | 103 ms: 1.03x faster                                                        |
| sympy_expand            | 475 ms                                                 | 460 ms: 1.03x faster                                                        |
| raytrace                | 297 ms                                                 | 288 ms: 1.03x faster                                                        |
| pprint_pformat          | 1.46 sec                                               | 1.41 sec: 1.03x faster                                                      |
| pyflate                 | 418 ms                                                 | 406 ms: 1.03x faster                                                        |
| sqlglot_normalize       | 108 ms                                                 | 105 ms: 1.03x faster                                                        |
| chaos                   | 69.2 ms                                                | 67.3 ms: 1.03x faster                                                       |
| genshi_text             | 21.6 ms                                                | 21.1 ms: 1.02x faster                                                       |
| hexiom                  | 6.37 ms                                                | 6.24 ms: 1.02x faster                                                       |
| deepcopy                | 342 us                                                 | 335 us: 1.02x faster                                                        |
| chameleon               | 6.47 ms                                                | 6.34 ms: 1.02x faster                                                       |
| docutils                | 2.63 sec                                               | 2.57 sec: 1.02x faster                                                      |
| regex_v8                | 22.0 ms                                                | 21.6 ms: 1.02x faster                                                       |
| pathlib                 | 18.2 ms                                                | 17.9 ms: 1.02x faster                                                       |
| scimark_lu              | 110 ms                                                 | 108 ms: 1.02x faster                                                        |
| crypto_pyaes            | 74.7 ms                                                | 73.5 ms: 1.02x faster                                                       |
| go                      | 140 ms                                                 | 138 ms: 1.02x faster                                                        |
| pprint_safe_repr        | 701 ms                                                 | 692 ms: 1.01x faster                                                        |
| xml_etree_iterparse     | 104 ms                                                 | 103 ms: 1.01x faster                                                        |
| tornado_http            | 96.3 ms                                                | 95.5 ms: 1.01x faster                                                       |
| create_gc_cycles        | 1.49 ms                                                | 1.48 ms: 1.01x faster                                                       |
| deepcopy_reduce         | 2.94 us                                                | 2.96 us: 1.01x slower                                                       |
| async_tree_io           | 1.30 sec                                               | 1.31 sec: 1.01x slower                                                      |
| django_template         | 32.6 ms                                                | 33.1 ms: 1.02x slower                                                       |
| regex_dna               | 204 ms                                                 | 208 ms: 1.02x slower                                                        |
| sqlglot_transpile       | 1.70 ms                                                | 1.74 ms: 1.02x slower                                                       |
| pickle_dict             | 31.1 us                                                | 31.8 us: 1.02x slower                                                       |
| sqlite_synth            | 2.52 us                                                | 2.58 us: 1.02x slower                                                       |
| sqlglot_parse           | 1.40 ms                                                | 1.44 ms: 1.03x slower                                                       |
| async_tree_memoization  | 627 ms                                                 | 646 ms: 1.03x slower                                                        |
| pickle_list             | 4.11 us                                                | 4.26 us: 1.04x slower                                                       |
| unpickle_list           | 4.91 us                                                | 5.13 us: 1.05x slower                                                       |
| xml_etree_process       | 53.9 ms                                                | 56.5 ms: 1.05x slower                                                       |
| python_startup          | 8.52 ms                                                | 9.00 ms: 1.06x slower                                                       |
| xml_etree_generate      | 76.2 ms                                                | 82.5 ms: 1.08x slower                                                       |
| python_startup_no_site  | 6.01 ms                                                | 6.53 ms: 1.09x slower                                                       |
| async_generators        | 368 ms                                                 | 411 ms: 1.12x slower                                                        |
| dask                    | 360 ms                                                 | 503 ms: 1.40x slower                                                        |
| Geometric mean          | (ref)                                                  | 1.05x faster                                                                |

Benchmark hidden because not significant (12): unpickle, telco, sqlalchemy_declarative, async_tree_none, djangocms, bench_mp_pool, nbody, async_tree_cpu_io_mixed, dulwich_log, thrift, sqlalchemy_imperative, pickle
Ignored benchmarks (7) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, comprehensions, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x
