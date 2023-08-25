
# Results vs. 3.10.4

- fork: eduardo-elizondo
- ref: immortal_references
- machine: linux-x86_64
- commit hash: 030016a
- commit date: 2023-04-06
- overall geometric mean: 1.22x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.16x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230406-linux-x86_64-eduardo%2delizondo-immortal_references-3.12.0a6+-030016a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 271 ms: 1.24x faster                                                              |
| chameleon      | 9.06 ms                                                | 6.94 ms: 1.31x faster                                                             |
| docutils       | 3.17 sec                                               | 2.80 sec: 1.13x faster                                                            |
| html5lib       | 85.9 ms                                                | 66.6 ms: 1.29x faster                                                             |
| tornado_http   | 127 ms                                                 | 104 ms: 1.23x faster                                                              |
| Geometric mean | (ref)                                                  | 1.24x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230406-linux-x86_64-eduardo%2delizondo-immortal_references-3.12.0a6+-030016a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 91.1 ms: 1.55x faster                                                             |
| float          | 111 ms                                                 | 81.0 ms: 1.36x faster                                                             |
| pidigits       | 190 ms                                                 | 197 ms: 1.04x slower                                                              |
| Geometric mean | (ref)                                                  | 1.27x faster                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230406-linux-x86_64-eduardo%2delizondo-immortal_references-3.12.0a6+-030016a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 148 ms: 1.19x faster                                                              |
| regex_v8       | 25.0 ms                                                | 21.9 ms: 1.14x faster                                                             |
| regex_dna      | 222 ms                                                 | 203 ms: 1.09x faster                                                              |
| regex_effbot   | 3.23 ms                                                | 3.61 ms: 1.12x slower                                                             |
| Geometric mean | (ref)                                                  | 1.07x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230406-linux-x86_64-eduardo%2delizondo-immortal_references-3.12.0a6+-030016a |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 316 us: 1.44x faster                                                              |
| unpickle_pure_python | 300 us                                                 | 219 us: 1.37x faster                                                              |
| json_dumps           | 13.5 ms                                                | 9.96 ms: 1.36x faster                                                             |
| xml_etree_process    | 74.9 ms                                                | 59.0 ms: 1.27x faster                                                             |
| xml_etree_generate   | 94.2 ms                                                | 84.1 ms: 1.12x faster                                                             |
| json_loads           | 28.8 us                                                | 25.8 us: 1.12x faster                                                             |
| xml_etree_iterparse  | 111 ms                                                 | 102 ms: 1.09x faster                                                              |
| xml_etree_parse      | 163 ms                                                 | 151 ms: 1.08x faster                                                              |
| unpickle             | 14.1 us                                                | 13.5 us: 1.05x faster                                                             |
| pickle_list          | 4.56 us                                                | 4.45 us: 1.02x faster                                                             |
| pickle               | 10.3 us                                                | 10.7 us: 1.04x slower                                                             |
| unpickle_list        | 4.82 us                                                | 5.14 us: 1.07x slower                                                             |
| pickle_dict          | 27.3 us                                                | 31.0 us: 1.14x slower                                                             |
| Geometric mean       | (ref)                                                  | 1.12x faster                                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230406-linux-x86_64-eduardo%2delizondo-immortal_references-3.12.0a6+-030016a |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.02 ms: 1.57x faster                                                             |
| python_startup_no_site | 5.82 ms                                                | 6.59 ms: 1.13x slower                                                             |
| Geometric mean         | (ref)                                                  | 1.18x faster                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230406-linux-x86_64-eduardo%2delizondo-immortal_references-3.12.0a6+-030016a |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 11.0 ms: 1.34x faster                                                             |
| genshi_text     | 30.3 ms                                                | 22.9 ms: 1.33x faster                                                             |
| django_template | 45.9 ms                                                | 35.6 ms: 1.29x faster                                                             |
| genshi_xml      | 63.3 ms                                                | 50.5 ms: 1.25x faster                                                             |
| Geometric mean  | (ref)                                                  | 1.30x faster                                                                      |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230406-linux-x86_64-eduardo%2delizondo-immortal_references-3.12.0a6+-030016a |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| generators              | 76.8 ms                                                | 31.8 ms: 2.41x faster                                                             |
| deltablue               | 7.42 ms                                                | 3.59 ms: 2.07x faster                                                             |
| asyncio_tcp             | 925 ms                                                 | 517 ms: 1.79x faster                                                              |
| logging_silent          | 175 ns                                                 | 103 ns: 1.71x faster                                                              |
| go                      | 229 ms                                                 | 140 ms: 1.64x faster                                                              |
| richards                | 74.9 ms                                                | 45.9 ms: 1.63x faster                                                             |
| python_startup          | 14.2 ms                                                | 9.02 ms: 1.57x faster                                                             |
| raytrace                | 464 ms                                                 | 298 ms: 1.56x faster                                                              |
| nbody                   | 142 ms                                                 | 91.1 ms: 1.55x faster                                                             |
| chaos                   | 106 ms                                                 | 70.5 ms: 1.51x faster                                                             |
| scimark_monte_carlo     | 108 ms                                                 | 71.9 ms: 1.51x faster                                                             |
| hexiom                  | 9.53 ms                                                | 6.33 ms: 1.50x faster                                                             |
| crypto_pyaes            | 118 ms                                                 | 80.0 ms: 1.48x faster                                                             |
| pyflate                 | 673 ms                                                 | 464 ms: 1.45x faster                                                              |
| pickle_pure_python      | 455 us                                                 | 316 us: 1.44x faster                                                              |
| scimark_lu              | 163 ms                                                 | 114 ms: 1.44x faster                                                              |
| scimark_sor             | 197 ms                                                 | 137 ms: 1.44x faster                                                              |
| spectral_norm           | 150 ms                                                 | 107 ms: 1.41x faster                                                              |
| coroutines              | 31.8 ms                                                | 22.8 ms: 1.40x faster                                                             |
| unpickle_pure_python    | 300 us                                                 | 219 us: 1.37x faster                                                              |
| float                   | 111 ms                                                 | 81.0 ms: 1.36x faster                                                             |
| deepcopy_memo           | 52.3 us                                                | 38.5 us: 1.36x faster                                                             |
| json_dumps              | 13.5 ms                                                | 9.96 ms: 1.36x faster                                                             |
| async_tree_io           | 1.77 sec                                               | 1.31 sec: 1.35x faster                                                            |
| mako                    | 14.8 ms                                                | 11.0 ms: 1.34x faster                                                             |
| async_tree_none         | 717 ms                                                 | 539 ms: 1.33x faster                                                              |
| genshi_text             | 30.3 ms                                                | 22.9 ms: 1.33x faster                                                             |
| pprint_pformat          | 1.99 sec                                               | 1.50 sec: 1.32x faster                                                            |
| sqlglot_parse           | 2.06 ms                                                | 1.57 ms: 1.31x faster                                                             |
| chameleon               | 9.06 ms                                                | 6.94 ms: 1.31x faster                                                             |
| pprint_safe_repr        | 955 ms                                                 | 737 ms: 1.30x faster                                                              |
| pycparser               | 1.50 sec                                               | 1.16 sec: 1.29x faster                                                            |
| django_template         | 45.9 ms                                                | 35.6 ms: 1.29x faster                                                             |
| html5lib                | 85.9 ms                                                | 66.6 ms: 1.29x faster                                                             |
| thrift                  | 1.03 ms                                                | 802 us: 1.29x faster                                                              |
| sqlglot_transpile       | 2.45 ms                                                | 1.90 ms: 1.29x faster                                                             |
| logging_format          | 8.91 us                                                | 7.00 us: 1.27x faster                                                             |
| logging_simple          | 8.07 us                                                | 6.35 us: 1.27x faster                                                             |
| xml_etree_process       | 74.9 ms                                                | 59.0 ms: 1.27x faster                                                             |
| async_tree_memoization  | 854 ms                                                 | 680 ms: 1.26x faster                                                              |
| genshi_xml              | 63.3 ms                                                | 50.5 ms: 1.25x faster                                                             |
| async_tree_cpu_io_mixed | 951 ms                                                 | 761 ms: 1.25x faster                                                              |
| fannkuch                | 486 ms                                                 | 391 ms: 1.24x faster                                                              |
| 2to3                    | 336 ms                                                 | 271 ms: 1.24x faster                                                              |
| tornado_http            | 127 ms                                                 | 104 ms: 1.23x faster                                                              |
| nqueens                 | 100 ms                                                 | 81.9 ms: 1.22x faster                                                             |
| unpack_sequence         | 64.7 ns                                                | 53.0 ns: 1.22x faster                                                             |
| scimark_fft             | 424 ms                                                 | 352 ms: 1.20x faster                                                              |
| deepcopy                | 442 us                                                 | 367 us: 1.20x faster                                                              |
| regex_compile           | 177 ms                                                 | 148 ms: 1.19x faster                                                              |
| sqlglot_normalize       | 135 ms                                                 | 115 ms: 1.18x faster                                                              |
| sqlglot_optimize        | 65.3 ms                                                | 55.6 ms: 1.18x faster                                                             |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.64 ms: 1.18x faster                                                             |
| mypy2                   | 428 ms                                                 | 366 ms: 1.17x faster                                                              |
| deepcopy_reduce         | 3.82 us                                                | 3.26 us: 1.17x faster                                                             |
| regex_v8                | 25.0 ms                                                | 21.9 ms: 1.14x faster                                                             |
| docutils                | 3.17 sec                                               | 2.80 sec: 1.13x faster                                                            |
| create_gc_cycles        | 1.67 ms                                                | 1.48 ms: 1.13x faster                                                             |
| bench_thread_pool       | 947 us                                                 | 838 us: 1.13x faster                                                              |
| xml_etree_generate      | 94.2 ms                                                | 84.1 ms: 1.12x faster                                                             |
| json_loads              | 28.8 us                                                | 25.8 us: 1.12x faster                                                             |
| sqlalchemy_declarative  | 165 ms                                                 | 149 ms: 1.11x faster                                                              |
| sympy_integrate         | 24.3 ms                                                | 22.2 ms: 1.09x faster                                                             |
| regex_dna               | 222 ms                                                 | 203 ms: 1.09x faster                                                              |
| xml_etree_iterparse     | 111 ms                                                 | 102 ms: 1.09x faster                                                              |
| dulwich_log             | 75.9 ms                                                | 69.8 ms: 1.09x faster                                                             |
| sqlite_synth            | 2.93 us                                                | 2.70 us: 1.09x faster                                                             |
| pathlib                 | 20.0 ms                                                | 18.5 ms: 1.08x faster                                                             |
| xml_etree_parse         | 163 ms                                                 | 151 ms: 1.08x faster                                                              |
| sympy_expand            | 545 ms                                                 | 506 ms: 1.08x faster                                                              |
| sqlalchemy_imperative   | 21.2 ms                                                | 19.8 ms: 1.07x faster                                                             |
| comprehensions          | 26.8 us                                                | 25.1 us: 1.07x faster                                                             |
| djangocms               | 35.9 us                                                | 34.1 us: 1.05x faster                                                             |
| mdp                     | 2.82 sec                                               | 2.68 sec: 1.05x faster                                                            |
| json                    | 5.42 ms                                                | 5.15 ms: 1.05x faster                                                             |
| unpickle                | 14.1 us                                                | 13.5 us: 1.05x faster                                                             |
| gc_traversal            | 3.84 ms                                                | 3.66 ms: 1.05x faster                                                             |
| sympy_str               | 328 ms                                                 | 319 ms: 1.03x faster                                                              |
| pickle_list             | 4.56 us                                                | 4.45 us: 1.02x faster                                                             |
| meteor_contest          | 115 ms                                                 | 113 ms: 1.01x faster                                                              |
| sympy_sum               | 185 ms                                                 | 183 ms: 1.01x faster                                                              |
| async_generators        | 425 ms                                                 | 429 ms: 1.01x slower                                                              |
| telco                   | 6.54 ms                                                | 6.73 ms: 1.03x slower                                                             |
| pidigits                | 190 ms                                                 | 197 ms: 1.04x slower                                                              |
| pickle                  | 10.3 us                                                | 10.7 us: 1.04x slower                                                             |
| unpickle_list           | 4.82 us                                                | 5.14 us: 1.07x slower                                                             |
| regex_effbot            | 3.23 ms                                                | 3.61 ms: 1.12x slower                                                             |
| python_startup_no_site  | 5.82 ms                                                | 6.59 ms: 1.13x slower                                                             |
| pickle_dict             | 27.3 us                                                | 31.0 us: 1.14x slower                                                             |
| dask                    | 423 ms                                                 | 555 ms: 1.31x slower                                                              |
| coverage                | 72.8 ms                                                | 98.5 ms: 1.35x slower                                                             |
| Geometric mean          | (ref)                                                  | 1.22x faster                                                                      |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.19x
- 95% likely to have a speedup of 1.18x
- 99% likely to have a speedup of 1.16x
