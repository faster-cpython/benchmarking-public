
# Results vs. 3.10.4

- fork: eduardo-elizondo
- ref: immortal_references
- machine: windows-amd64
- commit hash: 030016a
- commit date: 2023-04-06
- overall geometric mean: 1.03x faster \*
- HPT reliability: 95.91%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230406-pythonperf1-amd64-eduardo%2delizondo-immortal_references-3.12.0a6+-030016a |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| 2to3           | 237 ms                                                      | 234 ms: 1.01x faster                                                                   |
| chameleon      | 5.92 ms                                                     | 6.13 ms: 1.03x slower                                                                  |
| docutils       | 1.89 sec                                                    | 1.70 sec: 1.11x faster                                                                 |
| html5lib       | 46.5 ms                                                     | 42.8 ms: 1.09x faster                                                                  |
| tornado_http   | 109 ms                                                      | 95.8 ms: 1.14x faster                                                                  |
| Geometric mean | (ref)                                                       | 1.06x faster                                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230406-pythonperf1-amd64-eduardo%2delizondo-immortal_references-3.12.0a6+-030016a |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| float          | 60.2 ms                                                     | 62.4 ms: 1.04x slower                                                                  |
| pidigits       | 145 ms                                                      | 152 ms: 1.05x slower                                                                   |
| nbody          | 69.3 ms                                                     | 92.3 ms: 1.33x slower                                                                  |
| Geometric mean | (ref)                                                       | 1.13x slower                                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230406-pythonperf1-amd64-eduardo%2delizondo-immortal_references-3.12.0a6+-030016a |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| regex_dna      | 132 ms                                                      | 116 ms: 1.14x faster                                                                   |
| regex_effbot   | 1.66 ms                                                     | 1.50 ms: 1.11x faster                                                                  |
| regex_v8       | 15.0 ms                                                     | 13.8 ms: 1.09x faster                                                                  |
| Geometric mean | (ref)                                                       | 1.08x faster                                                                           |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230406-pythonperf1-amd64-eduardo%2delizondo-immortal_references-3.12.0a6+-030016a |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| json_dumps           | 8.50 ms                                                     | 5.78 ms: 1.47x faster                                                                  |
| unpickle             | 9.17 us                                                     | 7.80 us: 1.18x faster                                                                  |
| unpickle_list        | 2.81 us                                                     | 2.59 us: 1.08x faster                                                                  |
| xml_etree_parse      | 102 ms                                                      | 94.4 ms: 1.08x faster                                                                  |
| pickle_pure_python   | 257 us                                                      | 239 us: 1.07x faster                                                                   |
| json_loads           | 14.2 us                                                     | 13.9 us: 1.02x faster                                                                  |
| unpickle_pure_python | 171 us                                                      | 173 us: 1.01x slower                                                                   |
| xml_etree_process    | 43.4 ms                                                     | 44.2 ms: 1.02x slower                                                                  |
| xml_etree_iterparse  | 63.5 ms                                                     | 67.4 ms: 1.06x slower                                                                  |
| pickle               | 6.80 us                                                     | 7.23 us: 1.06x slower                                                                  |
| xml_etree_generate   | 54.5 ms                                                     | 60.6 ms: 1.11x slower                                                                  |
| pickle_dict          | 16.9 us                                                     | 19.6 us: 1.16x slower                                                                  |
| pickle_list          | 2.59 us                                                     | 3.10 us: 1.20x slower                                                                  |
| Geometric mean       | (ref)                                                       | 1.02x faster                                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230406-pythonperf1-amd64-eduardo%2delizondo-immortal_references-3.12.0a6+-030016a |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| python_startup         | 20.0 ms                                                     | 18.9 ms: 1.06x faster                                                                  |
| python_startup_no_site | 15.5 ms                                                     | 15.8 ms: 1.02x slower                                                                  |
| Geometric mean         | (ref)                                                       | 1.02x faster                                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230406-pythonperf1-amd64-eduardo%2delizondo-immortal_references-3.12.0a6+-030016a |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| mako            | 8.80 ms                                                     | 7.79 ms: 1.13x faster                                                                  |
| django_template | 28.2 ms                                                     | 25.3 ms: 1.12x faster                                                                  |
| genshi_text     | 19.0 ms                                                     | 17.5 ms: 1.09x faster                                                                  |
| genshi_xml      | 40.5 ms                                                     | 38.2 ms: 1.06x faster                                                                  |
| Geometric mean  | (ref)                                                       | 1.10x faster                                                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230406-pythonperf1-amd64-eduardo%2delizondo-immortal_references-3.12.0a6+-030016a |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| deltablue               | 4.17 ms                                                     | 2.70 ms: 1.54x faster                                                                  |
| json_dumps              | 8.50 ms                                                     | 5.78 ms: 1.47x faster                                                                  |
| asyncio_tcp             | 712 ms                                                      | 492 ms: 1.45x faster                                                                   |
| mypy2                   | 352 ms                                                      | 246 ms: 1.43x faster                                                                   |
| generators              | 31.6 ms                                                     | 22.5 ms: 1.41x faster                                                                  |
| async_tree_io           | 1.07 sec                                                    | 802 ms: 1.33x faster                                                                   |
| logging_silent          | 96.4 ns                                                     | 73.9 ns: 1.30x faster                                                                  |
| thrift                  | 615 us                                                      | 494 us: 1.24x faster                                                                   |
| go                      | 136 ms                                                      | 110 ms: 1.24x faster                                                                   |
| async_tree_none         | 420 ms                                                      | 342 ms: 1.23x faster                                                                   |
| async_tree_memoization  | 497 ms                                                      | 407 ms: 1.22x faster                                                                   |
| raytrace                | 271 ms                                                      | 223 ms: 1.21x faster                                                                   |
| async_tree_cpu_io_mixed | 609 ms                                                      | 502 ms: 1.21x faster                                                                   |
| richards                | 41.2 ms                                                     | 33.9 ms: 1.21x faster                                                                  |
| unpickle                | 9.17 us                                                     | 7.80 us: 1.18x faster                                                                  |
| scimark_lu              | 85.4 ms                                                     | 73.2 ms: 1.17x faster                                                                  |
| mdp                     | 1.71 sec                                                    | 1.50 sec: 1.14x faster                                                                 |
| regex_dna               | 132 ms                                                      | 116 ms: 1.14x faster                                                                   |
| tornado_http            | 109 ms                                                      | 95.8 ms: 1.14x faster                                                                  |
| mako                    | 8.80 ms                                                     | 7.79 ms: 1.13x faster                                                                  |
| pycparser               | 868 ms                                                      | 776 ms: 1.12x faster                                                                   |
| django_template         | 28.2 ms                                                     | 25.3 ms: 1.12x faster                                                                  |
| docutils                | 1.89 sec                                                    | 1.70 sec: 1.11x faster                                                                 |
| regex_effbot            | 1.66 ms                                                     | 1.50 ms: 1.11x faster                                                                  |
| crypto_pyaes            | 62.3 ms                                                     | 56.3 ms: 1.11x faster                                                                  |
| create_gc_cycles        | 782 us                                                      | 711 us: 1.10x faster                                                                   |
| json                    | 3.05 ms                                                     | 2.78 ms: 1.10x faster                                                                  |
| genshi_text             | 19.0 ms                                                     | 17.5 ms: 1.09x faster                                                                  |
| regex_v8                | 15.0 ms                                                     | 13.8 ms: 1.09x faster                                                                  |
| html5lib                | 46.5 ms                                                     | 42.8 ms: 1.09x faster                                                                  |
| pyflate                 | 387 ms                                                      | 357 ms: 1.08x faster                                                                   |
| unpickle_list           | 2.81 us                                                     | 2.59 us: 1.08x faster                                                                  |
| sqlglot_parse           | 1.22 ms                                                     | 1.13 ms: 1.08x faster                                                                  |
| xml_etree_parse         | 102 ms                                                      | 94.4 ms: 1.08x faster                                                                  |
| chaos                   | 58.9 ms                                                     | 54.8 ms: 1.07x faster                                                                  |
| pickle_pure_python      | 257 us                                                      | 239 us: 1.07x faster                                                                   |
| sqlglot_optimize        | 39.0 ms                                                     | 36.6 ms: 1.06x faster                                                                  |
| genshi_xml              | 40.5 ms                                                     | 38.2 ms: 1.06x faster                                                                  |
| dulwich_log             | 47.6 ms                                                     | 45.0 ms: 1.06x faster                                                                  |
| bench_thread_pool       | 946 us                                                      | 897 us: 1.06x faster                                                                   |
| python_startup          | 20.0 ms                                                     | 18.9 ms: 1.06x faster                                                                  |
| sqlglot_transpile       | 1.46 ms                                                     | 1.39 ms: 1.05x faster                                                                  |
| sympy_expand            | 315 ms                                                      | 302 ms: 1.04x faster                                                                   |
| hexiom                  | 5.52 ms                                                     | 5.32 ms: 1.04x faster                                                                  |
| sqlglot_normalize       | 202 ms                                                      | 196 ms: 1.03x faster                                                                   |
| json_loads              | 14.2 us                                                     | 13.9 us: 1.02x faster                                                                  |
| 2to3                    | 237 ms                                                      | 234 ms: 1.01x faster                                                                   |
| nqueens                 | 67.0 ms                                                     | 67.5 ms: 1.01x slower                                                                  |
| unpickle_pure_python    | 171 us                                                      | 173 us: 1.01x slower                                                                   |
| sympy_sum               | 104 ms                                                      | 106 ms: 1.01x slower                                                                   |
| xml_etree_process       | 43.4 ms                                                     | 44.2 ms: 1.02x slower                                                                  |
| sympy_str               | 188 ms                                                      | 192 ms: 1.02x slower                                                                   |
| python_startup_no_site  | 15.5 ms                                                     | 15.8 ms: 1.02x slower                                                                  |
| sqlite_synth            | 1.84 us                                                     | 1.87 us: 1.02x slower                                                                  |
| coroutines              | 15.9 ms                                                     | 16.4 ms: 1.03x slower                                                                  |
| chameleon               | 5.92 ms                                                     | 6.13 ms: 1.03x slower                                                                  |
| float                   | 60.2 ms                                                     | 62.4 ms: 1.04x slower                                                                  |
| spectral_norm           | 78.0 ms                                                     | 81.1 ms: 1.04x slower                                                                  |
| deepcopy_memo           | 28.5 us                                                     | 29.8 us: 1.05x slower                                                                  |
| pidigits                | 145 ms                                                      | 152 ms: 1.05x slower                                                                   |
| xml_etree_iterparse     | 63.5 ms                                                     | 67.4 ms: 1.06x slower                                                                  |
| pickle                  | 6.80 us                                                     | 7.23 us: 1.06x slower                                                                  |
| async_generators        | 224 ms                                                      | 239 ms: 1.07x slower                                                                   |
| deepcopy                | 255 us                                                      | 278 us: 1.09x slower                                                                   |
| deepcopy_reduce         | 2.16 us                                                     | 2.35 us: 1.09x slower                                                                  |
| pathlib                 | 77.4 ms                                                     | 85.3 ms: 1.10x slower                                                                  |
| xml_etree_generate      | 54.5 ms                                                     | 60.6 ms: 1.11x slower                                                                  |
| gc_traversal            | 1.34 ms                                                     | 1.52 ms: 1.13x slower                                                                  |
| logging_format          | 6.66 us                                                     | 7.54 us: 1.13x slower                                                                  |
| bench_mp_pool           | 60.7 ms                                                     | 68.7 ms: 1.13x slower                                                                  |
| scimark_sparse_mat_mult | 2.66 ms                                                     | 3.02 ms: 1.14x slower                                                                  |
| scimark_fft             | 193 ms                                                      | 220 ms: 1.14x slower                                                                   |
| telco                   | 3.78 ms                                                     | 4.31 ms: 1.14x slower                                                                  |
| comprehensions          | 16.0 us                                                     | 18.5 us: 1.16x slower                                                                  |
| pickle_dict             | 16.9 us                                                     | 19.6 us: 1.16x slower                                                                  |
| meteor_contest          | 72.5 ms                                                     | 85.3 ms: 1.18x slower                                                                  |
| logging_simple          | 6.20 us                                                     | 7.36 us: 1.19x slower                                                                  |
| pickle_list             | 2.59 us                                                     | 3.10 us: 1.20x slower                                                                  |
| fannkuch                | 258 ms                                                      | 313 ms: 1.21x slower                                                                   |
| nbody                   | 69.3 ms                                                     | 92.3 ms: 1.33x slower                                                                  |
| coverage                | 40.0 ms                                                     | 53.8 ms: 1.34x slower                                                                  |
| dask                    | 305 ms                                                      | 417 ms: 1.37x slower                                                                   |
| unpack_sequence         | 37.8 ns                                                     | 61.7 ns: 1.63x slower                                                                  |
| Geometric mean          | (ref)                                                       | 1.03x faster                                                                           |

Benchmark hidden because not significant (6): scimark_sor, regex_compile, pprint_safe_repr, scimark_monte_carlo, pprint_pformat, sympy_integrate
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 95.91% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x
