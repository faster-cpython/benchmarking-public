
# Results vs. 3.10.4

- fork: ericsnowcurrently
- ref: isolate_interned_dic
- machine: linux-x86_64
- commit hash: e53ac85
- commit date: 2023-03-27
- overall geometric mean: 1.30x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230327-linux-x86_64-ericsnowcurrently-isolate_interned_dic-3.12.0a6+-e53ac85 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 253 ms: 1.33x faster                                                              |
| chameleon      | 9.06 ms                                                | 6.43 ms: 1.41x faster                                                             |
| docutils       | 3.17 sec                                               | 2.53 sec: 1.25x faster                                                            |
| html5lib       | 85.9 ms                                                | 62.2 ms: 1.38x faster                                                             |
| tornado_http   | 127 ms                                                 | 91.5 ms: 1.39x faster                                                             |
| Geometric mean | (ref)                                                  | 1.35x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230327-linux-x86_64-ericsnowcurrently-isolate_interned_dic-3.12.0a6+-e53ac85 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 87.1 ms: 1.62x faster                                                             |
| float          | 111 ms                                                 | 73.8 ms: 1.50x faster                                                             |
| pidigits       | 190 ms                                                 | 188 ms: 1.01x faster                                                              |
| Geometric mean | (ref)                                                  | 1.35x faster                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230327-linux-x86_64-ericsnowcurrently-isolate_interned_dic-3.12.0a6+-e53ac85 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 134 ms: 1.32x faster                                                              |
| regex_v8       | 25.0 ms                                                | 21.7 ms: 1.16x faster                                                             |
| regex_dna      | 222 ms                                                 | 205 ms: 1.08x faster                                                              |
| regex_effbot   | 3.23 ms                                                | 3.73 ms: 1.16x slower                                                             |
| Geometric mean | (ref)                                                  | 1.09x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230327-linux-x86_64-ericsnowcurrently-isolate_interned_dic-3.12.0a6+-e53ac85 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 285 us: 1.60x faster                                                              |
| unpickle_pure_python | 300 us                                                 | 203 us: 1.48x faster                                                              |
| json_dumps           | 13.5 ms                                                | 9.53 ms: 1.42x faster                                                             |
| xml_etree_process    | 74.9 ms                                                | 55.4 ms: 1.35x faster                                                             |
| json_loads           | 28.8 us                                                | 24.3 us: 1.19x faster                                                             |
| xml_etree_generate   | 94.2 ms                                                | 80.2 ms: 1.17x faster                                                             |
| xml_etree_iterparse  | 111 ms                                                 | 98.5 ms: 1.13x faster                                                             |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.10x faster                                                              |
| pickle_list          | 4.56 us                                                | 4.13 us: 1.10x faster                                                             |
| unpickle             | 14.1 us                                                | 13.5 us: 1.05x faster                                                             |
| unpickle_list        | 4.82 us                                                | 4.99 us: 1.04x slower                                                             |
| pickle_dict          | 27.3 us                                                | 31.1 us: 1.14x slower                                                             |
| Geometric mean       | (ref)                                                  | 1.17x faster                                                                      |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230327-linux-x86_64-ericsnowcurrently-isolate_interned_dic-3.12.0a6+-e53ac85 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.85 ms: 1.60x faster                                                             |
| python_startup_no_site | 5.82 ms                                                | 6.54 ms: 1.12x slower                                                             |
| Geometric mean         | (ref)                                                  | 1.19x faster                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230327-linux-x86_64-ericsnowcurrently-isolate_interned_dic-3.12.0a6+-e53ac85 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.99 ms: 1.48x faster                                                             |
| genshi_text     | 30.3 ms                                                | 21.0 ms: 1.44x faster                                                             |
| django_template | 45.9 ms                                                | 33.7 ms: 1.36x faster                                                             |
| genshi_xml      | 63.3 ms                                                | 47.1 ms: 1.35x faster                                                             |
| Geometric mean  | (ref)                                                  | 1.41x faster                                                                      |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230327-linux-x86_64-ericsnowcurrently-isolate_interned_dic-3.12.0a6+-e53ac85 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| generators              | 76.8 ms                                                | 28.7 ms: 2.67x faster                                                             |
| deltablue               | 7.42 ms                                                | 3.23 ms: 2.30x faster                                                             |
| logging_silent          | 175 ns                                                 | 95.2 ns: 1.84x faster                                                             |
| asyncio_tcp             | 925 ms                                                 | 506 ms: 1.83x faster                                                              |
| scimark_sor             | 197 ms                                                 | 113 ms: 1.73x faster                                                              |
| richards                | 74.9 ms                                                | 44.0 ms: 1.70x faster                                                             |
| raytrace                | 464 ms                                                 | 280 ms: 1.66x faster                                                              |
| go                      | 229 ms                                                 | 140 ms: 1.64x faster                                                              |
| scimark_monte_carlo     | 108 ms                                                 | 66.3 ms: 1.63x faster                                                             |
| nbody                   | 142 ms                                                 | 87.1 ms: 1.62x faster                                                             |
| spectral_norm           | 150 ms                                                 | 93.1 ms: 1.61x faster                                                             |
| pyflate                 | 673 ms                                                 | 420 ms: 1.60x faster                                                              |
| python_startup          | 14.2 ms                                                | 8.85 ms: 1.60x faster                                                             |
| pickle_pure_python      | 455 us                                                 | 285 us: 1.60x faster                                                              |
| crypto_pyaes            | 118 ms                                                 | 74.5 ms: 1.59x faster                                                             |
| chaos                   | 106 ms                                                 | 67.4 ms: 1.58x faster                                                             |
| hexiom                  | 9.53 ms                                                | 6.08 ms: 1.57x faster                                                             |
| unpack_sequence         | 64.7 ns                                                | 42.0 ns: 1.54x faster                                                             |
| deepcopy_memo           | 52.3 us                                                | 34.6 us: 1.51x faster                                                             |
| scimark_lu              | 163 ms                                                 | 109 ms: 1.50x faster                                                              |
| float                   | 111 ms                                                 | 73.8 ms: 1.50x faster                                                             |
| unpickle_pure_python    | 300 us                                                 | 203 us: 1.48x faster                                                              |
| mako                    | 14.8 ms                                                | 9.99 ms: 1.48x faster                                                             |
| sqlglot_parse           | 2.06 ms                                                | 1.42 ms: 1.45x faster                                                             |
| genshi_text             | 30.3 ms                                                | 21.0 ms: 1.44x faster                                                             |
| sqlglot_transpile       | 2.45 ms                                                | 1.71 ms: 1.43x faster                                                             |
| json_dumps              | 13.5 ms                                                | 9.53 ms: 1.42x faster                                                             |
| logging_format          | 8.91 us                                                | 6.31 us: 1.41x faster                                                             |
| chameleon               | 9.06 ms                                                | 6.43 ms: 1.41x faster                                                             |
| logging_simple          | 8.07 us                                                | 5.77 us: 1.40x faster                                                             |
| scimark_fft             | 424 ms                                                 | 303 ms: 1.40x faster                                                              |
| pprint_pformat          | 1.99 sec                                               | 1.42 sec: 1.39x faster                                                            |
| tornado_http            | 127 ms                                                 | 91.5 ms: 1.39x faster                                                             |
| html5lib                | 85.9 ms                                                | 62.2 ms: 1.38x faster                                                             |
| pprint_safe_repr        | 955 ms                                                 | 693 ms: 1.38x faster                                                              |
| aiohttp                 | 1.38 ms                                                | 1.01 ms: 1.37x faster                                                             |
| django_template         | 45.9 ms                                                | 33.7 ms: 1.36x faster                                                             |
| async_tree_io           | 1.77 sec                                               | 1.30 sec: 1.36x faster                                                            |
| coroutines              | 31.8 ms                                                | 23.4 ms: 1.36x faster                                                             |
| async_tree_none         | 717 ms                                                 | 528 ms: 1.36x faster                                                              |
| xml_etree_process       | 74.9 ms                                                | 55.4 ms: 1.35x faster                                                             |
| pycparser               | 1.50 sec                                               | 1.11 sec: 1.35x faster                                                            |
| deepcopy                | 442 us                                                 | 328 us: 1.35x faster                                                              |
| genshi_xml              | 63.3 ms                                                | 47.1 ms: 1.35x faster                                                             |
| gunicorn                | 1.46 ms                                                | 1.10 ms: 1.33x faster                                                             |
| 2to3                    | 336 ms                                                 | 253 ms: 1.33x faster                                                              |
| thrift                  | 1.03 ms                                                | 779 us: 1.33x faster                                                              |
| regex_compile           | 177 ms                                                 | 134 ms: 1.32x faster                                                              |
| deepcopy_reduce         | 3.82 us                                                | 2.91 us: 1.31x faster                                                             |
| async_tree_memoization  | 854 ms                                                 | 656 ms: 1.30x faster                                                              |
| fannkuch                | 486 ms                                                 | 375 ms: 1.29x faster                                                              |
| mypy2                   | 428 ms                                                 | 333 ms: 1.29x faster                                                              |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.24 ms: 1.29x faster                                                             |
| async_tree_cpu_io_mixed | 951 ms                                                 | 745 ms: 1.28x faster                                                              |
| sqlglot_normalize       | 135 ms                                                 | 106 ms: 1.28x faster                                                              |
| sqlglot_optimize        | 65.3 ms                                                | 51.5 ms: 1.27x faster                                                             |
| nqueens                 | 100 ms                                                 | 79.8 ms: 1.25x faster                                                             |
| docutils                | 3.17 sec                                               | 2.53 sec: 1.25x faster                                                            |
| sqlalchemy_declarative  | 165 ms                                                 | 136 ms: 1.22x faster                                                              |
| sqlalchemy_imperative   | 21.2 ms                                                | 17.7 ms: 1.19x faster                                                             |
| bench_thread_pool       | 947 us                                                 | 793 us: 1.19x faster                                                              |
| sympy_integrate         | 24.3 ms                                                | 20.4 ms: 1.19x faster                                                             |
| json_loads              | 28.8 us                                                | 24.3 us: 1.19x faster                                                             |
| dulwich_log             | 75.9 ms                                                | 64.0 ms: 1.19x faster                                                             |
| sympy_expand            | 545 ms                                                 | 461 ms: 1.18x faster                                                              |
| xml_etree_generate      | 94.2 ms                                                | 80.2 ms: 1.17x faster                                                             |
| json                    | 5.42 ms                                                | 4.65 ms: 1.17x faster                                                             |
| sympy_str               | 328 ms                                                 | 283 ms: 1.16x faster                                                              |
| regex_v8                | 25.0 ms                                                | 21.7 ms: 1.16x faster                                                             |
| create_gc_cycles        | 1.67 ms                                                | 1.47 ms: 1.14x faster                                                             |
| xml_etree_iterparse     | 111 ms                                                 | 98.5 ms: 1.13x faster                                                             |
| comprehensions          | 26.8 us                                                | 23.8 us: 1.13x faster                                                             |
| mdp                     | 2.82 sec                                               | 2.50 sec: 1.13x faster                                                            |
| sqlite_synth            | 2.93 us                                                | 2.61 us: 1.12x faster                                                             |
| meteor_contest          | 115 ms                                                 | 103 ms: 1.12x faster                                                              |
| sympy_sum               | 185 ms                                                 | 166 ms: 1.11x faster                                                              |
| djangocms               | 35.9 us                                                | 32.4 us: 1.11x faster                                                             |
| pathlib                 | 20.0 ms                                                | 18.1 ms: 1.11x faster                                                             |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.10x faster                                                              |
| pickle_list             | 4.56 us                                                | 4.13 us: 1.10x faster                                                             |
| gc_traversal            | 3.84 ms                                                | 3.53 ms: 1.09x faster                                                             |
| regex_dna               | 222 ms                                                 | 205 ms: 1.08x faster                                                              |
| unpickle                | 14.1 us                                                | 13.5 us: 1.05x faster                                                             |
| async_generators        | 425 ms                                                 | 413 ms: 1.03x faster                                                              |
| pidigits                | 190 ms                                                 | 188 ms: 1.01x faster                                                              |
| unpickle_list           | 4.82 us                                                | 4.99 us: 1.04x slower                                                             |
| python_startup_no_site  | 5.82 ms                                                | 6.54 ms: 1.12x slower                                                             |
| pickle_dict             | 27.3 us                                                | 31.1 us: 1.14x slower                                                             |
| regex_effbot            | 3.23 ms                                                | 3.73 ms: 1.16x slower                                                             |
| dask                    | 423 ms                                                 | 509 ms: 1.21x slower                                                              |
| coverage                | 72.8 ms                                                | 97.3 ms: 1.34x slower                                                             |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                                      |

Benchmark hidden because not significant (3): telco, bench_mp_pool, pickle
Ignored benchmarks (6) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.29x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.25x
