
# Results vs. 3.11.0

- fork: iritkatriel
- ref: object_init
- machine: linux-x86_64
- commit hash: 1a4b9a9
- commit date: 2023-02-08
- overall geometric mean: 1.05x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230208-linux-x86_64-iritkatriel-object_init-3.12.0a5+-1a4b9a9 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 251 ms: 1.03x faster                                               |
| chameleon      | 6.47 ms                                                | 6.36 ms: 1.02x faster                                              |
| docutils       | 2.63 sec                                               | 2.56 sec: 1.03x faster                                             |
| html5lib       | 64.5 ms                                                | 60.9 ms: 1.06x faster                                              |
| tornado_http   | 96.3 ms                                                | 94.0 ms: 1.02x faster                                              |
| Geometric mean | (ref)                                                  | 1.03x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230208-linux-x86_64-iritkatriel-object_init-3.12.0a5+-1a4b9a9 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| nbody          | 93.1 ms                                                | 86.0 ms: 1.08x faster                                              |
| float          | 77.2 ms                                                | 72.1 ms: 1.07x faster                                              |
| pidigits       | 198 ms                                                 | 190 ms: 1.04x faster                                               |
| Geometric mean | (ref)                                                  | 1.07x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230208-linux-x86_64-iritkatriel-object_init-3.12.0a5+-1a4b9a9 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.32 ms: 1.20x faster                                              |
| regex_compile  | 138 ms                                                 | 128 ms: 1.08x faster                                               |
| regex_v8       | 22.0 ms                                                | 21.4 ms: 1.03x faster                                              |
| regex_dna      | 204 ms                                                 | 211 ms: 1.03x slower                                               |
| Geometric mean | (ref)                                                  | 1.07x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230208-linux-x86_64-iritkatriel-object_init-3.12.0a5+-1a4b9a9 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.34 ms: 1.35x faster                                              |
| unpickle_pure_python | 228 us                                                 | 197 us: 1.16x faster                                               |
| json_loads           | 26.5 us                                                | 23.7 us: 1.12x faster                                              |
| xml_etree_parse      | 158 ms                                                 | 149 ms: 1.07x faster                                               |
| pickle_pure_python   | 306 us                                                 | 288 us: 1.06x faster                                               |
| unpickle             | 13.7 us                                                | 13.1 us: 1.04x faster                                              |
| pickle_dict          | 31.1 us                                                | 30.6 us: 1.02x faster                                              |
| pickle_list          | 4.11 us                                                | 4.09 us: 1.01x faster                                              |
| pickle               | 10.1 us                                                | 10.2 us: 1.01x slower                                              |
| unpickle_list        | 4.91 us                                                | 5.04 us: 1.03x slower                                              |
| xml_etree_process    | 53.9 ms                                                | 55.6 ms: 1.03x slower                                              |
| xml_etree_iterparse  | 104 ms                                                 | 108 ms: 1.04x slower                                               |
| xml_etree_generate   | 76.2 ms                                                | 81.3 ms: 1.07x slower                                              |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230208-linux-x86_64-iritkatriel-object_init-3.12.0a5+-1a4b9a9 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.97 ms: 1.05x slower                                              |
| python_startup_no_site | 6.01 ms                                                | 6.51 ms: 1.08x slower                                              |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230208-linux-x86_64-iritkatriel-object_init-3.12.0a5+-1a4b9a9 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 46.4 ms: 1.12x faster                                              |
| mako            | 10.1 ms                                                | 9.65 ms: 1.05x faster                                              |
| genshi_text     | 21.6 ms                                                | 20.7 ms: 1.04x faster                                              |
| django_template | 32.6 ms                                                | 32.4 ms: 1.01x faster                                              |
| Geometric mean  | (ref)                                                  | 1.05x faster                                                       |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230208-linux-x86_64-iritkatriel-object_init-3.12.0a5+-1a4b9a9 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| asyncio_tcp             | 922 ms                                                 | 490 ms: 1.88x faster                                               |
| json_dumps              | 12.6 ms                                                | 9.34 ms: 1.35x faster                                              |
| mypy2                   | 420 ms                                                 | 328 ms: 1.28x faster                                               |
| regex_effbot            | 3.99 ms                                                | 3.32 ms: 1.20x faster                                              |
| unpickle_pure_python    | 228 us                                                 | 197 us: 1.16x faster                                               |
| deltablue               | 3.67 ms                                                | 3.18 ms: 1.16x faster                                              |
| scimark_sparse_mat_mult | 4.50 ms                                                | 3.90 ms: 1.15x faster                                              |
| genshi_xml              | 51.8 ms                                                | 46.4 ms: 1.12x faster                                              |
| json_loads              | 26.5 us                                                | 23.7 us: 1.12x faster                                              |
| scimark_fft             | 328 ms                                                 | 298 ms: 1.10x faster                                               |
| scimark_sor             | 118 ms                                                 | 108 ms: 1.10x faster                                               |
| logging_silent          | 101 ns                                                 | 92.3 ns: 1.10x faster                                              |
| aiohttp                 | 1.10 ms                                                | 1.00 ms: 1.09x faster                                              |
| deepcopy_memo           | 37.0 us                                                | 33.9 us: 1.09x faster                                              |
| gunicorn                | 1.18 ms                                                | 1.08 ms: 1.09x faster                                              |
| richards                | 45.7 ms                                                | 42.2 ms: 1.08x faster                                              |
| nbody                   | 93.1 ms                                                | 86.0 ms: 1.08x faster                                              |
| regex_compile           | 138 ms                                                 | 128 ms: 1.08x faster                                               |
| chaos                   | 69.2 ms                                                | 64.1 ms: 1.08x faster                                              |
| pycparser               | 1.18 sec                                               | 1.10 sec: 1.08x faster                                             |
| sympy_str               | 290 ms                                                 | 271 ms: 1.07x faster                                               |
| float                   | 77.2 ms                                                | 72.1 ms: 1.07x faster                                              |
| hexiom                  | 6.37 ms                                                | 5.95 ms: 1.07x faster                                              |
| mdp                     | 2.62 sec                                               | 2.45 sec: 1.07x faster                                             |
| xml_etree_parse         | 158 ms                                                 | 149 ms: 1.07x faster                                               |
| json                    | 4.94 ms                                                | 4.64 ms: 1.07x faster                                              |
| pickle_pure_python      | 306 us                                                 | 288 us: 1.06x faster                                               |
| html5lib                | 64.5 ms                                                | 60.9 ms: 1.06x faster                                              |
| nqueens                 | 83.4 ms                                                | 78.8 ms: 1.06x faster                                              |
| raytrace                | 297 ms                                                 | 281 ms: 1.06x faster                                               |
| sympy_integrate         | 21.0 ms                                                | 19.8 ms: 1.06x faster                                              |
| logging_format          | 6.68 us                                                | 6.34 us: 1.05x faster                                              |
| sympy_sum               | 167 ms                                                 | 158 ms: 1.05x faster                                               |
| fannkuch                | 388 ms                                                 | 369 ms: 1.05x faster                                               |
| crypto_pyaes            | 74.7 ms                                                | 71.3 ms: 1.05x faster                                              |
| scimark_monte_carlo     | 68.1 ms                                                | 65.0 ms: 1.05x faster                                              |
| mako                    | 10.1 ms                                                | 9.65 ms: 1.05x faster                                              |
| pprint_pformat          | 1.46 sec                                               | 1.40 sec: 1.04x faster                                             |
| spectral_norm           | 100 ms                                                 | 95.9 ms: 1.04x faster                                              |
| pidigits                | 198 ms                                                 | 190 ms: 1.04x faster                                               |
| bench_thread_pool       | 819 us                                                 | 786 us: 1.04x faster                                               |
| deepcopy                | 342 us                                                 | 328 us: 1.04x faster                                               |
| sqlglot_optimize        | 53.1 ms                                                | 51.0 ms: 1.04x faster                                              |
| logging_simple          | 6.03 us                                                | 5.79 us: 1.04x faster                                              |
| coroutines              | 25.5 ms                                                | 24.5 ms: 1.04x faster                                              |
| unpickle                | 13.7 us                                                | 13.1 us: 1.04x faster                                              |
| sympy_expand            | 475 ms                                                 | 457 ms: 1.04x faster                                               |
| genshi_text             | 21.6 ms                                                | 20.7 ms: 1.04x faster                                              |
| pyflate                 | 418 ms                                                 | 403 ms: 1.04x faster                                               |
| go                      | 140 ms                                                 | 135 ms: 1.04x faster                                               |
| 2to3                    | 259 ms                                                 | 251 ms: 1.03x faster                                               |
| pprint_safe_repr        | 701 ms                                                 | 680 ms: 1.03x faster                                               |
| regex_v8                | 22.0 ms                                                | 21.4 ms: 1.03x faster                                              |
| scimark_lu              | 110 ms                                                 | 106 ms: 1.03x faster                                               |
| coverage                | 100 ms                                                 | 97.3 ms: 1.03x faster                                              |
| telco                   | 6.58 ms                                                | 6.40 ms: 1.03x faster                                              |
| docutils                | 2.63 sec                                               | 2.56 sec: 1.03x faster                                             |
| djangocms               | 32.4 us                                                | 31.6 us: 1.03x faster                                              |
| pathlib                 | 18.2 ms                                                | 17.8 ms: 1.02x faster                                              |
| tornado_http            | 96.3 ms                                                | 94.0 ms: 1.02x faster                                              |
| sqlglot_normalize       | 108 ms                                                 | 105 ms: 1.02x faster                                               |
| pickle_dict             | 31.1 us                                                | 30.6 us: 1.02x faster                                              |
| chameleon               | 6.47 ms                                                | 6.36 ms: 1.02x faster                                              |
| gc_traversal            | 4.02 ms                                                | 3.96 ms: 1.02x faster                                              |
| sqlalchemy_declarative  | 138 ms                                                 | 137 ms: 1.01x faster                                               |
| create_gc_cycles        | 1.49 ms                                                | 1.47 ms: 1.01x faster                                              |
| dulwich_log             | 63.7 ms                                                | 63.1 ms: 1.01x faster                                              |
| django_template         | 32.6 ms                                                | 32.4 ms: 1.01x faster                                              |
| deepcopy_reduce         | 2.94 us                                                | 2.92 us: 1.01x faster                                              |
| pickle_list             | 4.11 us                                                | 4.09 us: 1.01x faster                                              |
| sqlglot_transpile       | 1.70 ms                                                | 1.72 ms: 1.01x slower                                              |
| sqlglot_parse           | 1.40 ms                                                | 1.41 ms: 1.01x slower                                              |
| thrift                  | 756 us                                                 | 765 us: 1.01x slower                                               |
| pickle                  | 10.1 us                                                | 10.2 us: 1.01x slower                                              |
| sqlite_synth            | 2.52 us                                                | 2.56 us: 1.02x slower                                              |
| async_tree_cpu_io_mixed | 739 ms                                                 | 752 ms: 1.02x slower                                               |
| unpickle_list           | 4.91 us                                                | 5.04 us: 1.03x slower                                              |
| xml_etree_process       | 53.9 ms                                                | 55.6 ms: 1.03x slower                                              |
| regex_dna               | 204 ms                                                 | 211 ms: 1.03x slower                                               |
| generators              | 73.5 ms                                                | 76.5 ms: 1.04x slower                                              |
| xml_etree_iterparse     | 104 ms                                                 | 108 ms: 1.04x slower                                               |
| python_startup          | 8.52 ms                                                | 8.97 ms: 1.05x slower                                              |
| xml_etree_generate      | 76.2 ms                                                | 81.3 ms: 1.07x slower                                              |
| python_startup_no_site  | 6.01 ms                                                | 6.51 ms: 1.08x slower                                              |
| async_generators        | 368 ms                                                 | 423 ms: 1.15x slower                                               |
| Geometric mean          | (ref)                                                  | 1.05x faster                                                       |

Benchmark hidden because not significant (7): unpack_sequence, async_tree_none, bench_mp_pool, async_tree_io, sqlalchemy_imperative, meteor_contest, async_tree_memoization
Ignored benchmarks (8) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, comprehensions, dask, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x
