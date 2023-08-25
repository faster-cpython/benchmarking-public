
# Results vs. 3.10.4

- fork: ericsnowcurrently
- ref: isolate_dict_global_
- machine: linux-x86_64
- commit hash: f707a1b
- commit date: 2023-02-28
- overall geometric mean: 1.29x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_dict_global_-3.12.0a5+-f707a1b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 251 ms: 1.34x faster                                                              |
| chameleon      | 9.06 ms                                                | 6.28 ms: 1.44x faster                                                             |
| docutils       | 3.17 sec                                               | 2.57 sec: 1.23x faster                                                            |
| html5lib       | 85.9 ms                                                | 61.7 ms: 1.39x faster                                                             |
| tornado_http   | 127 ms                                                 | 95.5 ms: 1.33x faster                                                             |
| Geometric mean | (ref)                                                  | 1.35x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_dict_global_-3.12.0a5+-f707a1b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 93.9 ms: 1.51x faster                                                             |
| float          | 111 ms                                                 | 74.3 ms: 1.49x faster                                                             |
| pidigits       | 190 ms                                                 | 189 ms: 1.00x faster                                                              |
| Geometric mean | (ref)                                                  | 1.31x faster                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_dict_global_-3.12.0a5+-f707a1b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 133 ms: 1.33x faster                                                              |
| regex_v8       | 25.0 ms                                                | 21.9 ms: 1.14x faster                                                             |
| regex_dna      | 222 ms                                                 | 210 ms: 1.06x faster                                                              |
| regex_effbot   | 3.23 ms                                                | 3.63 ms: 1.12x slower                                                             |
| Geometric mean | (ref)                                                  | 1.09x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_dict_global_-3.12.0a5+-f707a1b |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 282 us: 1.62x faster                                                              |
| unpickle_pure_python | 300 us                                                 | 199 us: 1.51x faster                                                              |
| json_dumps           | 13.5 ms                                                | 9.55 ms: 1.42x faster                                                             |
| xml_etree_process    | 74.9 ms                                                | 55.6 ms: 1.35x faster                                                             |
| json_loads           | 28.8 us                                                | 24.3 us: 1.19x faster                                                             |
| xml_etree_generate   | 94.2 ms                                                | 80.8 ms: 1.17x faster                                                             |
| pickle_list          | 4.56 us                                                | 4.09 us: 1.11x faster                                                             |
| xml_etree_parse      | 163 ms                                                 | 149 ms: 1.09x faster                                                              |
| xml_etree_iterparse  | 111 ms                                                 | 104 ms: 1.07x faster                                                              |
| unpickle             | 14.1 us                                                | 13.6 us: 1.04x faster                                                             |
| pickle               | 10.3 us                                                | 10.2 us: 1.01x faster                                                             |
| unpickle_list        | 4.82 us                                                | 4.96 us: 1.03x slower                                                             |
| pickle_dict          | 27.3 us                                                | 30.8 us: 1.13x slower                                                             |
| Geometric mean       | (ref)                                                  | 1.17x faster                                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_dict_global_-3.12.0a5+-f707a1b |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.06 ms: 1.56x faster                                                             |
| python_startup_no_site | 5.82 ms                                                | 6.57 ms: 1.13x slower                                                             |
| Geometric mean         | (ref)                                                  | 1.18x faster                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_dict_global_-3.12.0a5+-f707a1b |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.81 ms: 1.50x faster                                                             |
| genshi_text     | 30.3 ms                                                | 21.4 ms: 1.42x faster                                                             |
| django_template | 45.9 ms                                                | 33.0 ms: 1.39x faster                                                             |
| genshi_xml      | 63.3 ms                                                | 48.6 ms: 1.30x faster                                                             |
| Geometric mean  | (ref)                                                  | 1.40x faster                                                                      |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_dict_global_-3.12.0a5+-f707a1b |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| generators              | 76.8 ms                                                | 30.6 ms: 2.51x faster                                                             |
| deltablue               | 7.42 ms                                                | 3.21 ms: 2.31x faster                                                             |
| scimark_sor             | 197 ms                                                 | 106 ms: 1.85x faster                                                              |
| logging_silent          | 175 ns                                                 | 94.5 ns: 1.85x faster                                                             |
| asyncio_tcp             | 925 ms                                                 | 503 ms: 1.84x faster                                                              |
| richards                | 74.9 ms                                                | 43.2 ms: 1.73x faster                                                             |
| go                      | 229 ms                                                 | 135 ms: 1.70x faster                                                              |
| scimark_monte_carlo     | 108 ms                                                 | 66.6 ms: 1.63x faster                                                             |
| pickle_pure_python      | 455 us                                                 | 282 us: 1.62x faster                                                              |
| pyflate                 | 673 ms                                                 | 417 ms: 1.61x faster                                                              |
| crypto_pyaes            | 118 ms                                                 | 73.6 ms: 1.61x faster                                                             |
| raytrace                | 464 ms                                                 | 289 ms: 1.61x faster                                                              |
| spectral_norm           | 150 ms                                                 | 93.8 ms: 1.60x faster                                                             |
| python_startup          | 14.2 ms                                                | 9.06 ms: 1.56x faster                                                             |
| chaos                   | 106 ms                                                 | 68.5 ms: 1.55x faster                                                             |
| hexiom                  | 9.53 ms                                                | 6.16 ms: 1.55x faster                                                             |
| deepcopy_memo           | 52.3 us                                                | 34.1 us: 1.54x faster                                                             |
| unpickle_pure_python    | 300 us                                                 | 199 us: 1.51x faster                                                              |
| nbody                   | 142 ms                                                 | 93.9 ms: 1.51x faster                                                             |
| mako                    | 14.8 ms                                                | 9.81 ms: 1.50x faster                                                             |
| scimark_lu              | 163 ms                                                 | 110 ms: 1.49x faster                                                              |
| float                   | 111 ms                                                 | 74.3 ms: 1.49x faster                                                             |
| unpack_sequence         | 64.7 ns                                                | 44.3 ns: 1.46x faster                                                             |
| chameleon               | 9.06 ms                                                | 6.28 ms: 1.44x faster                                                             |
| logging_format          | 8.91 us                                                | 6.27 us: 1.42x faster                                                             |
| pprint_pformat          | 1.99 sec                                               | 1.40 sec: 1.42x faster                                                            |
| genshi_text             | 30.3 ms                                                | 21.4 ms: 1.42x faster                                                             |
| json_dumps              | 13.5 ms                                                | 9.55 ms: 1.42x faster                                                             |
| sqlglot_parse           | 2.06 ms                                                | 1.46 ms: 1.41x faster                                                             |
| pprint_safe_repr        | 955 ms                                                 | 679 ms: 1.41x faster                                                              |
| sqlglot_transpile       | 2.45 ms                                                | 1.75 ms: 1.40x faster                                                             |
| logging_simple          | 8.07 us                                                | 5.78 us: 1.40x faster                                                             |
| html5lib                | 85.9 ms                                                | 61.7 ms: 1.39x faster                                                             |
| django_template         | 45.9 ms                                                | 33.0 ms: 1.39x faster                                                             |
| async_tree_io           | 1.77 sec                                               | 1.28 sec: 1.38x faster                                                            |
| async_tree_none         | 717 ms                                                 | 523 ms: 1.37x faster                                                              |
| aiohttp                 | 1.38 ms                                                | 1.01 ms: 1.37x faster                                                             |
| scimark_fft             | 424 ms                                                 | 312 ms: 1.36x faster                                                              |
| coroutines              | 31.8 ms                                                | 23.5 ms: 1.35x faster                                                             |
| gunicorn                | 1.46 ms                                                | 1.08 ms: 1.35x faster                                                             |
| xml_etree_process       | 74.9 ms                                                | 55.6 ms: 1.35x faster                                                             |
| pycparser               | 1.50 sec                                               | 1.12 sec: 1.34x faster                                                            |
| fannkuch                | 486 ms                                                 | 362 ms: 1.34x faster                                                              |
| 2to3                    | 336 ms                                                 | 251 ms: 1.34x faster                                                              |
| deepcopy                | 442 us                                                 | 331 us: 1.34x faster                                                              |
| tornado_http            | 127 ms                                                 | 95.5 ms: 1.33x faster                                                             |
| regex_compile           | 177 ms                                                 | 133 ms: 1.33x faster                                                              |
| async_tree_memoization  | 854 ms                                                 | 650 ms: 1.32x faster                                                              |
| thrift                  | 1.03 ms                                                | 793 us: 1.30x faster                                                              |
| genshi_xml              | 63.3 ms                                                | 48.6 ms: 1.30x faster                                                             |
| deepcopy_reduce         | 3.82 us                                                | 2.95 us: 1.30x faster                                                             |
| async_tree_cpu_io_mixed | 951 ms                                                 | 737 ms: 1.29x faster                                                              |
| mypy2                   | 428 ms                                                 | 334 ms: 1.28x faster                                                              |
| sqlglot_normalize       | 135 ms                                                 | 106 ms: 1.28x faster                                                              |
| sqlglot_optimize        | 65.3 ms                                                | 51.6 ms: 1.27x faster                                                             |
| nqueens                 | 100 ms                                                 | 80.5 ms: 1.24x faster                                                             |
| docutils                | 3.17 sec                                               | 2.57 sec: 1.23x faster                                                            |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.42 ms: 1.23x faster                                                             |
| dulwich_log             | 75.9 ms                                                | 63.8 ms: 1.19x faster                                                             |
| sqlalchemy_declarative  | 165 ms                                                 | 139 ms: 1.19x faster                                                              |
| bench_thread_pool       | 947 us                                                 | 797 us: 1.19x faster                                                              |
| json_loads              | 28.8 us                                                | 24.3 us: 1.19x faster                                                             |
| mdp                     | 2.82 sec                                               | 2.40 sec: 1.18x faster                                                            |
| json                    | 5.42 ms                                                | 4.62 ms: 1.17x faster                                                             |
| sympy_expand            | 545 ms                                                 | 466 ms: 1.17x faster                                                              |
| sympy_integrate         | 24.3 ms                                                | 20.8 ms: 1.17x faster                                                             |
| xml_etree_generate      | 94.2 ms                                                | 80.8 ms: 1.17x faster                                                             |
| sqlalchemy_imperative   | 21.2 ms                                                | 18.2 ms: 1.16x faster                                                             |
| regex_v8                | 25.0 ms                                                | 21.9 ms: 1.14x faster                                                             |
| sympy_str               | 328 ms                                                 | 289 ms: 1.14x faster                                                              |
| pathlib                 | 20.0 ms                                                | 17.7 ms: 1.13x faster                                                             |
| sqlite_synth            | 2.93 us                                                | 2.63 us: 1.12x faster                                                             |
| create_gc_cycles        | 1.67 ms                                                | 1.50 ms: 1.12x faster                                                             |
| pickle_list             | 4.56 us                                                | 4.09 us: 1.11x faster                                                             |
| meteor_contest          | 115 ms                                                 | 103 ms: 1.11x faster                                                              |
| comprehensions          | 26.8 us                                                | 24.2 us: 1.11x faster                                                             |
| djangocms               | 35.9 us                                                | 32.6 us: 1.10x faster                                                             |
| sympy_sum               | 185 ms                                                 | 168 ms: 1.10x faster                                                              |
| xml_etree_parse         | 163 ms                                                 | 149 ms: 1.09x faster                                                              |
| xml_etree_iterparse     | 111 ms                                                 | 104 ms: 1.07x faster                                                              |
| regex_dna               | 222 ms                                                 | 210 ms: 1.06x faster                                                              |
| unpickle                | 14.1 us                                                | 13.6 us: 1.04x faster                                                             |
| telco                   | 6.54 ms                                                | 6.40 ms: 1.02x faster                                                             |
| async_generators        | 425 ms                                                 | 417 ms: 1.02x faster                                                              |
| pickle                  | 10.3 us                                                | 10.2 us: 1.01x faster                                                             |
| pidigits                | 190 ms                                                 | 189 ms: 1.00x faster                                                              |
| gc_traversal            | 3.84 ms                                                | 3.83 ms: 1.00x faster                                                             |
| unpickle_list           | 4.82 us                                                | 4.96 us: 1.03x slower                                                             |
| regex_effbot            | 3.23 ms                                                | 3.63 ms: 1.12x slower                                                             |
| pickle_dict             | 27.3 us                                                | 30.8 us: 1.13x slower                                                             |
| python_startup_no_site  | 5.82 ms                                                | 6.57 ms: 1.13x slower                                                             |
| dask                    | 423 ms                                                 | 510 ms: 1.21x slower                                                              |
| coverage                | 72.8 ms                                                | 93.1 ms: 1.28x slower                                                             |
| Geometric mean          | (ref)                                                  | 1.29x faster                                                                      |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (6) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.29x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.24x
