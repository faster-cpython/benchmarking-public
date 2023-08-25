
# Results vs. 3.11.0

- fork: brandtbucher
- ref: type_cache
- machine: linux-x86_64
- commit hash: c87e8bd
- commit date: 2023-03-22
- overall geometric mean: 1.03x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230322-linux-x86_64-brandtbucher-type_cache-3.12.0a6+-c87e8bd |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 253 ms: 1.02x faster                                               |
| chameleon      | 6.47 ms                                                | 6.64 ms: 1.03x slower                                              |
| docutils       | 2.63 sec                                               | 2.56 sec: 1.02x faster                                             |
| html5lib       | 64.5 ms                                                | 61.9 ms: 1.04x faster                                              |
| tornado_http   | 96.3 ms                                                | 91.7 ms: 1.05x faster                                              |
| Geometric mean | (ref)                                                  | 1.02x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230322-linux-x86_64-brandtbucher-type_cache-3.12.0a6+-c87e8bd |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| pidigits       | 198 ms                                                 | 188 ms: 1.05x faster                                               |
| float          | 77.2 ms                                                | 74.4 ms: 1.04x faster                                              |
| nbody          | 93.1 ms                                                | 90.6 ms: 1.03x faster                                              |
| Geometric mean | (ref)                                                  | 1.04x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230322-linux-x86_64-brandtbucher-type_cache-3.12.0a6+-c87e8bd |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.57 ms: 1.12x faster                                              |
| regex_compile  | 138 ms                                                 | 134 ms: 1.03x faster                                               |
| regex_dna      | 204 ms                                                 | 208 ms: 1.02x slower                                               |
| regex_v8       | 22.0 ms                                                | 22.8 ms: 1.03x slower                                              |
| Geometric mean | (ref)                                                  | 1.02x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230322-linux-x86_64-brandtbucher-type_cache-3.12.0a6+-c87e8bd |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.70 ms: 1.30x faster                                              |
| unpickle_pure_python | 228 us                                                 | 203 us: 1.12x faster                                               |
| json_loads           | 26.5 us                                                | 24.2 us: 1.09x faster                                              |
| pickle_pure_python   | 306 us                                                 | 290 us: 1.05x faster                                               |
| xml_etree_parse      | 158 ms                                                 | 152 ms: 1.05x faster                                               |
| xml_etree_iterparse  | 104 ms                                                 | 103 ms: 1.01x faster                                               |
| pickle_dict          | 31.1 us                                                | 31.1 us: 1.00x faster                                              |
| pickle               | 10.1 us                                                | 10.2 us: 1.02x slower                                              |
| pickle_list          | 4.11 us                                                | 4.21 us: 1.02x slower                                              |
| unpickle_list        | 4.91 us                                                | 5.20 us: 1.06x slower                                              |
| xml_etree_process    | 53.9 ms                                                | 57.3 ms: 1.06x slower                                              |
| xml_etree_generate   | 76.2 ms                                                | 81.7 ms: 1.07x slower                                              |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                       |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230322-linux-x86_64-brandtbucher-type_cache-3.12.0a6+-c87e8bd |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.88 ms: 1.04x slower                                              |
| python_startup_no_site | 6.01 ms                                                | 6.56 ms: 1.09x slower                                              |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230322-linux-x86_64-brandtbucher-type_cache-3.12.0a6+-c87e8bd |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 48.1 ms: 1.08x faster                                              |
| mako            | 10.1 ms                                                | 10.0 ms: 1.01x faster                                              |
| genshi_text     | 21.6 ms                                                | 21.8 ms: 1.01x slower                                              |
| django_template | 32.6 ms                                                | 33.2 ms: 1.02x slower                                              |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                       |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230322-linux-x86_64-brandtbucher-type_cache-3.12.0a6+-c87e8bd |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| generators              | 73.5 ms                                                | 29.4 ms: 2.50x faster                                              |
| asyncio_tcp             | 922 ms                                                 | 509 ms: 1.81x faster                                               |
| json_dumps              | 12.6 ms                                                | 9.70 ms: 1.30x faster                                              |
| mypy2                   | 420 ms                                                 | 336 ms: 1.25x faster                                               |
| coroutines              | 25.5 ms                                                | 22.5 ms: 1.13x faster                                              |
| unpickle_pure_python    | 228 us                                                 | 203 us: 1.12x faster                                               |
| regex_effbot            | 3.99 ms                                                | 3.57 ms: 1.12x faster                                              |
| spectral_norm           | 100 ms                                                 | 90.4 ms: 1.11x faster                                              |
| scimark_sor             | 118 ms                                                 | 107 ms: 1.10x faster                                               |
| deltablue               | 3.67 ms                                                | 3.33 ms: 1.10x faster                                              |
| json_loads              | 26.5 us                                                | 24.2 us: 1.09x faster                                              |
| genshi_xml              | 51.8 ms                                                | 48.1 ms: 1.08x faster                                              |
| scimark_fft             | 328 ms                                                 | 307 ms: 1.07x faster                                               |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.22 ms: 1.07x faster                                              |
| deepcopy_memo           | 37.0 us                                                | 34.9 us: 1.06x faster                                              |
| hexiom                  | 6.37 ms                                                | 6.04 ms: 1.06x faster                                              |
| pickle_pure_python      | 306 us                                                 | 290 us: 1.05x faster                                               |
| pidigits                | 198 ms                                                 | 188 ms: 1.05x faster                                               |
| json                    | 4.94 ms                                                | 4.70 ms: 1.05x faster                                              |
| tornado_http            | 96.3 ms                                                | 91.7 ms: 1.05x faster                                              |
| xml_etree_parse         | 158 ms                                                 | 152 ms: 1.05x faster                                               |
| logging_silent          | 101 ns                                                 | 97.0 ns: 1.04x faster                                              |
| html5lib                | 64.5 ms                                                | 61.9 ms: 1.04x faster                                              |
| mdp                     | 2.62 sec                                               | 2.51 sec: 1.04x faster                                             |
| go                      | 140 ms                                                 | 135 ms: 1.04x faster                                               |
| richards                | 45.7 ms                                                | 44.0 ms: 1.04x faster                                              |
| float                   | 77.2 ms                                                | 74.4 ms: 1.04x faster                                              |
| fannkuch                | 388 ms                                                 | 374 ms: 1.04x faster                                               |
| nqueens                 | 83.4 ms                                                | 80.5 ms: 1.04x faster                                              |
| logging_format          | 6.68 us                                                | 6.47 us: 1.03x faster                                              |
| chaos                   | 69.2 ms                                                | 67.0 ms: 1.03x faster                                              |
| bench_thread_pool       | 819 us                                                 | 794 us: 1.03x faster                                               |
| regex_compile           | 138 ms                                                 | 134 ms: 1.03x faster                                               |
| nbody                   | 93.1 ms                                                | 90.6 ms: 1.03x faster                                              |
| deepcopy                | 342 us                                                 | 333 us: 1.03x faster                                               |
| docutils                | 2.63 sec                                               | 2.56 sec: 1.02x faster                                             |
| logging_simple          | 6.03 us                                                | 5.90 us: 1.02x faster                                              |
| 2to3                    | 259 ms                                                 | 253 ms: 1.02x faster                                               |
| sympy_integrate         | 21.0 ms                                                | 20.5 ms: 1.02x faster                                              |
| pprint_pformat          | 1.46 sec                                               | 1.42 sec: 1.02x faster                                             |
| sympy_expand            | 475 ms                                                 | 465 ms: 1.02x faster                                               |
| sympy_str               | 290 ms                                                 | 284 ms: 1.02x faster                                               |
| pathlib                 | 18.2 ms                                                | 17.9 ms: 1.02x faster                                              |
| sqlglot_optimize        | 53.1 ms                                                | 52.2 ms: 1.02x faster                                              |
| pycparser               | 1.18 sec                                               | 1.16 sec: 1.01x faster                                             |
| xml_etree_iterparse     | 104 ms                                                 | 103 ms: 1.01x faster                                               |
| scimark_lu              | 110 ms                                                 | 108 ms: 1.01x faster                                               |
| raytrace                | 297 ms                                                 | 293 ms: 1.01x faster                                               |
| pprint_safe_repr        | 701 ms                                                 | 693 ms: 1.01x faster                                               |
| gc_traversal            | 4.02 ms                                                | 3.98 ms: 1.01x faster                                              |
| mako                    | 10.1 ms                                                | 10.0 ms: 1.01x faster                                              |
| pickle_dict             | 31.1 us                                                | 31.1 us: 1.00x faster                                              |
| async_tree_io           | 1.30 sec                                               | 1.31 sec: 1.01x slower                                             |
| crypto_pyaes            | 74.7 ms                                                | 75.3 ms: 1.01x slower                                              |
| genshi_text             | 21.6 ms                                                | 21.8 ms: 1.01x slower                                              |
| pickle                  | 10.1 us                                                | 10.2 us: 1.02x slower                                              |
| django_template         | 32.6 ms                                                | 33.2 ms: 1.02x slower                                              |
| regex_dna               | 204 ms                                                 | 208 ms: 1.02x slower                                               |
| unpack_sequence         | 43.1 ns                                                | 44.0 ns: 1.02x slower                                              |
| pickle_list             | 4.11 us                                                | 4.21 us: 1.02x slower                                              |
| chameleon               | 6.47 ms                                                | 6.64 ms: 1.03x slower                                              |
| sqlglot_transpile       | 1.70 ms                                                | 1.75 ms: 1.03x slower                                              |
| regex_v8                | 22.0 ms                                                | 22.8 ms: 1.03x slower                                              |
| sqlite_synth            | 2.52 us                                                | 2.62 us: 1.04x slower                                              |
| sqlglot_parse           | 1.40 ms                                                | 1.46 ms: 1.04x slower                                              |
| python_startup          | 8.52 ms                                                | 8.88 ms: 1.04x slower                                              |
| unpickle_list           | 4.91 us                                                | 5.20 us: 1.06x slower                                              |
| xml_etree_process       | 53.9 ms                                                | 57.3 ms: 1.06x slower                                              |
| async_tree_memoization  | 627 ms                                                 | 667 ms: 1.06x slower                                               |
| xml_etree_generate      | 76.2 ms                                                | 81.7 ms: 1.07x slower                                              |
| thrift                  | 756 us                                                 | 816 us: 1.08x slower                                               |
| comprehensions          | 22.4 us                                                | 24.4 us: 1.08x slower                                              |
| python_startup_no_site  | 6.01 ms                                                | 6.56 ms: 1.09x slower                                              |
| async_generators        | 368 ms                                                 | 417 ms: 1.13x slower                                               |
| dask                    | 360 ms                                                 | 509 ms: 1.42x slower                                               |
| Geometric mean          | (ref)                                                  | 1.03x faster                                                       |

Benchmark hidden because not significant (13): unpickle, meteor_contest, telco, dulwich_log, scimark_monte_carlo, sympy_sum, sqlglot_normalize, pyflate, bench_mp_pool, create_gc_cycles, deepcopy_reduce, async_tree_none, async_tree_cpu_io_mixed
Ignored benchmarks (12) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, coverage, djangocms, flaskblogging, gunicorn, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x
