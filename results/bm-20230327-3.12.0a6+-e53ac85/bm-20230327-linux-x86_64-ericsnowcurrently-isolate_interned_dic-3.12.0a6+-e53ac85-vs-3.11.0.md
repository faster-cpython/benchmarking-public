
# Results vs. 3.11.0

- fork: ericsnowcurrently
- ref: isolate_interned_dic
- machine: linux-x86_64
- commit hash: e53ac85
- commit date: 2023-03-27
- overall geometric mean: 1.04x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230327-linux-x86_64-ericsnowcurrently-isolate_interned_dic-3.12.0a6+-e53ac85 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 253 ms: 1.03x faster                                                              |
| chameleon      | 6.47 ms                                                | 6.43 ms: 1.01x faster                                                             |
| docutils       | 2.63 sec                                               | 2.53 sec: 1.04x faster                                                            |
| html5lib       | 64.5 ms                                                | 62.2 ms: 1.04x faster                                                             |
| tornado_http   | 96.3 ms                                                | 91.5 ms: 1.05x faster                                                             |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230327-linux-x86_64-ericsnowcurrently-isolate_interned_dic-3.12.0a6+-e53ac85 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| nbody          | 93.1 ms                                                | 87.1 ms: 1.07x faster                                                             |
| pidigits       | 198 ms                                                 | 188 ms: 1.05x faster                                                              |
| float          | 77.2 ms                                                | 73.8 ms: 1.05x faster                                                             |
| Geometric mean | (ref)                                                  | 1.06x faster                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230327-linux-x86_64-ericsnowcurrently-isolate_interned_dic-3.12.0a6+-e53ac85 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.73 ms: 1.07x faster                                                             |
| regex_compile  | 138 ms                                                 | 134 ms: 1.03x faster                                                              |
| regex_v8       | 22.0 ms                                                | 21.7 ms: 1.02x faster                                                             |
| regex_dna      | 204 ms                                                 | 205 ms: 1.00x slower                                                              |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230327-linux-x86_64-ericsnowcurrently-isolate_interned_dic-3.12.0a6+-e53ac85 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.53 ms: 1.32x faster                                                             |
| unpickle_pure_python | 228 us                                                 | 203 us: 1.13x faster                                                              |
| json_loads           | 26.5 us                                                | 24.3 us: 1.09x faster                                                             |
| pickle_pure_python   | 306 us                                                 | 285 us: 1.07x faster                                                              |
| xml_etree_parse      | 158 ms                                                 | 148 ms: 1.07x faster                                                              |
| xml_etree_iterparse  | 104 ms                                                 | 98.5 ms: 1.05x faster                                                             |
| pickle_list          | 4.11 us                                                | 4.13 us: 1.00x slower                                                             |
| unpickle_list        | 4.91 us                                                | 4.99 us: 1.02x slower                                                             |
| pickle               | 10.1 us                                                | 10.3 us: 1.02x slower                                                             |
| xml_etree_process    | 53.9 ms                                                | 55.4 ms: 1.03x slower                                                             |
| xml_etree_generate   | 76.2 ms                                                | 80.2 ms: 1.05x slower                                                             |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                                      |

Benchmark hidden because not significant (2): unpickle, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230327-linux-x86_64-ericsnowcurrently-isolate_interned_dic-3.12.0a6+-e53ac85 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.85 ms: 1.04x slower                                                             |
| python_startup_no_site | 6.01 ms                                                | 6.54 ms: 1.09x slower                                                             |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230327-linux-x86_64-ericsnowcurrently-isolate_interned_dic-3.12.0a6+-e53ac85 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 47.1 ms: 1.10x faster                                                             |
| genshi_text     | 21.6 ms                                                | 21.0 ms: 1.03x faster                                                             |
| mako            | 10.1 ms                                                | 9.99 ms: 1.01x faster                                                             |
| django_template | 32.6 ms                                                | 33.7 ms: 1.03x slower                                                             |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                                      |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230327-linux-x86_64-ericsnowcurrently-isolate_interned_dic-3.12.0a6+-e53ac85 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| generators              | 73.5 ms                                                | 28.7 ms: 2.56x faster                                                             |
| asyncio_tcp             | 922 ms                                                 | 506 ms: 1.82x faster                                                              |
| json_dumps              | 12.6 ms                                                | 9.53 ms: 1.32x faster                                                             |
| mypy2                   | 420 ms                                                 | 333 ms: 1.26x faster                                                              |
| gc_traversal            | 4.02 ms                                                | 3.53 ms: 1.14x faster                                                             |
| deltablue               | 3.67 ms                                                | 3.23 ms: 1.14x faster                                                             |
| unpickle_pure_python    | 228 us                                                 | 203 us: 1.13x faster                                                              |
| genshi_xml              | 51.8 ms                                                | 47.1 ms: 1.10x faster                                                             |
| coroutines              | 25.5 ms                                                | 23.4 ms: 1.09x faster                                                             |
| json_loads              | 26.5 us                                                | 24.3 us: 1.09x faster                                                             |
| aiohttp                 | 1.10 ms                                                | 1.01 ms: 1.09x faster                                                             |
| scimark_fft             | 328 ms                                                 | 303 ms: 1.08x faster                                                              |
| gunicorn                | 1.18 ms                                                | 1.10 ms: 1.07x faster                                                             |
| spectral_norm           | 100 ms                                                 | 93.1 ms: 1.07x faster                                                             |
| pickle_pure_python      | 306 us                                                 | 285 us: 1.07x faster                                                              |
| xml_etree_parse         | 158 ms                                                 | 148 ms: 1.07x faster                                                              |
| deepcopy_memo           | 37.0 us                                                | 34.6 us: 1.07x faster                                                             |
| regex_effbot            | 3.99 ms                                                | 3.73 ms: 1.07x faster                                                             |
| nbody                   | 93.1 ms                                                | 87.1 ms: 1.07x faster                                                             |
| json                    | 4.94 ms                                                | 4.65 ms: 1.06x faster                                                             |
| logging_silent          | 101 ns                                                 | 95.2 ns: 1.06x faster                                                             |
| pycparser               | 1.18 sec                                               | 1.11 sec: 1.06x faster                                                            |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.24 ms: 1.06x faster                                                             |
| raytrace                | 297 ms                                                 | 280 ms: 1.06x faster                                                              |
| logging_format          | 6.68 us                                                | 6.31 us: 1.06x faster                                                             |
| xml_etree_iterparse     | 104 ms                                                 | 98.5 ms: 1.05x faster                                                             |
| pidigits                | 198 ms                                                 | 188 ms: 1.05x faster                                                              |
| tornado_http            | 96.3 ms                                                | 91.5 ms: 1.05x faster                                                             |
| hexiom                  | 6.37 ms                                                | 6.08 ms: 1.05x faster                                                             |
| float                   | 77.2 ms                                                | 73.8 ms: 1.05x faster                                                             |
| mdp                     | 2.62 sec                                               | 2.50 sec: 1.05x faster                                                            |
| logging_simple          | 6.03 us                                                | 5.77 us: 1.05x faster                                                             |
| nqueens                 | 83.4 ms                                                | 79.8 ms: 1.05x faster                                                             |
| deepcopy                | 342 us                                                 | 328 us: 1.04x faster                                                              |
| scimark_sor             | 118 ms                                                 | 113 ms: 1.04x faster                                                              |
| richards                | 45.7 ms                                                | 44.0 ms: 1.04x faster                                                             |
| meteor_contest          | 107 ms                                                 | 103 ms: 1.04x faster                                                              |
| docutils                | 2.63 sec                                               | 2.53 sec: 1.04x faster                                                            |
| html5lib                | 64.5 ms                                                | 62.2 ms: 1.04x faster                                                             |
| fannkuch                | 388 ms                                                 | 375 ms: 1.03x faster                                                              |
| bench_thread_pool       | 819 us                                                 | 793 us: 1.03x faster                                                              |
| sympy_expand            | 475 ms                                                 | 461 ms: 1.03x faster                                                              |
| sqlglot_optimize        | 53.1 ms                                                | 51.5 ms: 1.03x faster                                                             |
| coverage                | 100 ms                                                 | 97.3 ms: 1.03x faster                                                             |
| regex_compile           | 138 ms                                                 | 134 ms: 1.03x faster                                                              |
| chaos                   | 69.2 ms                                                | 67.4 ms: 1.03x faster                                                             |
| sympy_integrate         | 21.0 ms                                                | 20.4 ms: 1.03x faster                                                             |
| scimark_monte_carlo     | 68.1 ms                                                | 66.3 ms: 1.03x faster                                                             |
| unpack_sequence         | 43.1 ns                                                | 42.0 ns: 1.03x faster                                                             |
| 2to3                    | 259 ms                                                 | 253 ms: 1.03x faster                                                              |
| sympy_str               | 290 ms                                                 | 283 ms: 1.03x faster                                                              |
| genshi_text             | 21.6 ms                                                | 21.0 ms: 1.03x faster                                                             |
| pprint_pformat          | 1.46 sec                                               | 1.42 sec: 1.02x faster                                                            |
| regex_v8                | 22.0 ms                                                | 21.7 ms: 1.02x faster                                                             |
| sqlglot_normalize       | 108 ms                                                 | 106 ms: 1.02x faster                                                              |
| sqlalchemy_declarative  | 138 ms                                                 | 136 ms: 1.02x faster                                                              |
| pprint_safe_repr        | 701 ms                                                 | 693 ms: 1.01x faster                                                              |
| create_gc_cycles        | 1.49 ms                                                | 1.47 ms: 1.01x faster                                                             |
| deepcopy_reduce         | 2.94 us                                                | 2.91 us: 1.01x faster                                                             |
| pathlib                 | 18.2 ms                                                | 18.1 ms: 1.01x faster                                                             |
| mako                    | 10.1 ms                                                | 9.99 ms: 1.01x faster                                                             |
| scimark_lu              | 110 ms                                                 | 109 ms: 1.01x faster                                                              |
| chameleon               | 6.47 ms                                                | 6.43 ms: 1.01x faster                                                             |
| sympy_sum               | 167 ms                                                 | 166 ms: 1.00x faster                                                              |
| crypto_pyaes            | 74.7 ms                                                | 74.5 ms: 1.00x faster                                                             |
| regex_dna               | 204 ms                                                 | 205 ms: 1.00x slower                                                              |
| pickle_list             | 4.11 us                                                | 4.13 us: 1.00x slower                                                             |
| pyflate                 | 418 ms                                                 | 420 ms: 1.01x slower                                                              |
| dulwich_log             | 63.7 ms                                                | 64.0 ms: 1.01x slower                                                             |
| sqlglot_parse           | 1.40 ms                                                | 1.42 ms: 1.01x slower                                                             |
| unpickle_list           | 4.91 us                                                | 4.99 us: 1.02x slower                                                             |
| pickle                  | 10.1 us                                                | 10.3 us: 1.02x slower                                                             |
| xml_etree_process       | 53.9 ms                                                | 55.4 ms: 1.03x slower                                                             |
| thrift                  | 756 us                                                 | 779 us: 1.03x slower                                                              |
| django_template         | 32.6 ms                                                | 33.7 ms: 1.03x slower                                                             |
| sqlite_synth            | 2.52 us                                                | 2.61 us: 1.04x slower                                                             |
| python_startup          | 8.52 ms                                                | 8.85 ms: 1.04x slower                                                             |
| async_tree_memoization  | 627 ms                                                 | 656 ms: 1.05x slower                                                              |
| xml_etree_generate      | 76.2 ms                                                | 80.2 ms: 1.05x slower                                                             |
| comprehensions          | 22.4 us                                                | 23.8 us: 1.06x slower                                                             |
| python_startup_no_site  | 6.01 ms                                                | 6.54 ms: 1.09x slower                                                             |
| async_generators        | 368 ms                                                 | 413 ms: 1.12x slower                                                              |
| dask                    | 360 ms                                                 | 509 ms: 1.42x slower                                                              |
| Geometric mean          | (ref)                                                  | 1.04x faster                                                                      |

Benchmark hidden because not significant (11): unpickle, sqlalchemy_imperative, telco, go, djangocms, bench_mp_pool, pickle_dict, async_tree_none, async_tree_io, sqlglot_transpile, async_tree_cpu_io_mixed
Ignored benchmarks (6) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x
