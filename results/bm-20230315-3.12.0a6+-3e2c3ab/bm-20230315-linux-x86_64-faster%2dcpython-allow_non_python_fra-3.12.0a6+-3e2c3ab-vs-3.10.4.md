
# Results vs. 3.10.4

- fork: faster-cpython
- ref: allow_non_python_fra
- machine: linux-x86_64
- commit hash: 3e2c3ab
- commit date: 2023-03-15
- overall geometric mean: 1.29x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230315-linux-x86_64-faster%2dcpython-allow_non_python_fra-3.12.0a6+-3e2c3ab |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 252 ms: 1.34x faster                                                             |
| chameleon      | 9.06 ms                                                | 6.42 ms: 1.41x faster                                                            |
| docutils       | 3.17 sec                                               | 2.55 sec: 1.24x faster                                                           |
| html5lib       | 85.9 ms                                                | 62.1 ms: 1.38x faster                                                            |
| tornado_http   | 127 ms                                                 | 95.2 ms: 1.34x faster                                                            |
| Geometric mean | (ref)                                                  | 1.34x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230315-linux-x86_64-faster%2dcpython-allow_non_python_fra-3.12.0a6+-3e2c3ab |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 95.6 ms: 1.48x faster                                                            |
| float          | 111 ms                                                 | 75.2 ms: 1.47x faster                                                            |
| pidigits       | 190 ms                                                 | 190 ms: 1.00x faster                                                             |
| Geometric mean | (ref)                                                  | 1.30x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230315-linux-x86_64-faster%2dcpython-allow_non_python_fra-3.12.0a6+-3e2c3ab |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 134 ms: 1.32x faster                                                             |
| regex_v8       | 25.0 ms                                                | 21.8 ms: 1.15x faster                                                            |
| regex_dna      | 222 ms                                                 | 203 ms: 1.09x faster                                                             |
| regex_effbot   | 3.23 ms                                                | 3.36 ms: 1.04x slower                                                            |
| Geometric mean | (ref)                                                  | 1.12x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230315-linux-x86_64-faster%2dcpython-allow_non_python_fra-3.12.0a6+-3e2c3ab |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 286 us: 1.59x faster                                                             |
| unpickle_pure_python | 300 us                                                 | 201 us: 1.49x faster                                                             |
| json_dumps           | 13.5 ms                                                | 9.55 ms: 1.42x faster                                                            |
| xml_etree_process    | 74.9 ms                                                | 55.2 ms: 1.36x faster                                                            |
| json_loads           | 28.8 us                                                | 24.4 us: 1.18x faster                                                            |
| xml_etree_generate   | 94.2 ms                                                | 81.0 ms: 1.16x faster                                                            |
| xml_etree_iterparse  | 111 ms                                                 | 99.4 ms: 1.12x faster                                                            |
| pickle_list          | 4.56 us                                                | 4.12 us: 1.11x faster                                                            |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.11x faster                                                             |
| pickle               | 10.3 us                                                | 10.2 us: 1.01x faster                                                            |
| unpickle_list        | 4.82 us                                                | 5.05 us: 1.05x slower                                                            |
| pickle_dict          | 27.3 us                                                | 31.1 us: 1.14x slower                                                            |
| Geometric mean       | (ref)                                                  | 1.17x faster                                                                     |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230315-linux-x86_64-faster%2dcpython-allow_non_python_fra-3.12.0a6+-3e2c3ab |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.02 ms: 1.57x faster                                                            |
| python_startup_no_site | 5.82 ms                                                | 6.54 ms: 1.12x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.18x faster                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230315-linux-x86_64-faster%2dcpython-allow_non_python_fra-3.12.0a6+-3e2c3ab |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 10.0 ms: 1.47x faster                                                            |
| genshi_text     | 30.3 ms                                                | 21.5 ms: 1.41x faster                                                            |
| django_template | 45.9 ms                                                | 33.5 ms: 1.37x faster                                                            |
| genshi_xml      | 63.3 ms                                                | 47.7 ms: 1.33x faster                                                            |
| Geometric mean  | (ref)                                                  | 1.40x faster                                                                     |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230315-linux-x86_64-faster%2dcpython-allow_non_python_fra-3.12.0a6+-3e2c3ab |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| generators              | 76.8 ms                                                | 29.3 ms: 2.62x faster                                                            |
| deltablue               | 7.42 ms                                                | 3.21 ms: 2.31x faster                                                            |
| scimark_sor             | 197 ms                                                 | 107 ms: 1.85x faster                                                             |
| logging_silent          | 175 ns                                                 | 96.1 ns: 1.82x faster                                                            |
| asyncio_tcp             | 925 ms                                                 | 515 ms: 1.80x faster                                                             |
| richards                | 74.9 ms                                                | 44.0 ms: 1.70x faster                                                            |
| go                      | 229 ms                                                 | 137 ms: 1.68x faster                                                             |
| pyflate                 | 673 ms                                                 | 409 ms: 1.65x faster                                                             |
| raytrace                | 464 ms                                                 | 287 ms: 1.62x faster                                                             |
| scimark_monte_carlo     | 108 ms                                                 | 67.8 ms: 1.60x faster                                                            |
| crypto_pyaes            | 118 ms                                                 | 74.2 ms: 1.60x faster                                                            |
| pickle_pure_python      | 455 us                                                 | 286 us: 1.59x faster                                                             |
| python_startup          | 14.2 ms                                                | 9.02 ms: 1.57x faster                                                            |
| chaos                   | 106 ms                                                 | 67.9 ms: 1.56x faster                                                            |
| spectral_norm           | 150 ms                                                 | 97.8 ms: 1.53x faster                                                            |
| deepcopy_memo           | 52.3 us                                                | 34.4 us: 1.52x faster                                                            |
| hexiom                  | 9.53 ms                                                | 6.27 ms: 1.52x faster                                                            |
| unpickle_pure_python    | 300 us                                                 | 201 us: 1.49x faster                                                             |
| nbody                   | 142 ms                                                 | 95.6 ms: 1.48x faster                                                            |
| unpack_sequence         | 64.7 ns                                                | 43.8 ns: 1.48x faster                                                            |
| mako                    | 14.8 ms                                                | 10.0 ms: 1.47x faster                                                            |
| float                   | 111 ms                                                 | 75.2 ms: 1.47x faster                                                            |
| scimark_lu              | 163 ms                                                 | 112 ms: 1.46x faster                                                             |
| sqlglot_parse           | 2.06 ms                                                | 1.44 ms: 1.43x faster                                                            |
| pprint_pformat          | 1.99 sec                                               | 1.39 sec: 1.42x faster                                                           |
| sqlglot_transpile       | 2.45 ms                                                | 1.72 ms: 1.42x faster                                                            |
| json_dumps              | 13.5 ms                                                | 9.55 ms: 1.42x faster                                                            |
| genshi_text             | 30.3 ms                                                | 21.5 ms: 1.41x faster                                                            |
| chameleon               | 9.06 ms                                                | 6.42 ms: 1.41x faster                                                            |
| pprint_safe_repr        | 955 ms                                                 | 683 ms: 1.40x faster                                                             |
| coroutines              | 31.8 ms                                                | 22.9 ms: 1.39x faster                                                            |
| logging_format          | 8.91 us                                                | 6.41 us: 1.39x faster                                                            |
| html5lib                | 85.9 ms                                                | 62.1 ms: 1.38x faster                                                            |
| logging_simple          | 8.07 us                                                | 5.86 us: 1.38x faster                                                            |
| aiohttp                 | 1.38 ms                                                | 1.01 ms: 1.37x faster                                                            |
| django_template         | 45.9 ms                                                | 33.5 ms: 1.37x faster                                                            |
| async_tree_none         | 717 ms                                                 | 526 ms: 1.36x faster                                                             |
| async_tree_io           | 1.77 sec                                               | 1.30 sec: 1.36x faster                                                           |
| xml_etree_process       | 74.9 ms                                                | 55.2 ms: 1.36x faster                                                            |
| tornado_http            | 127 ms                                                 | 95.2 ms: 1.34x faster                                                            |
| 2to3                    | 336 ms                                                 | 252 ms: 1.34x faster                                                             |
| gunicorn                | 1.46 ms                                                | 1.10 ms: 1.33x faster                                                            |
| pycparser               | 1.50 sec                                               | 1.13 sec: 1.33x faster                                                           |
| genshi_xml              | 63.3 ms                                                | 47.7 ms: 1.33x faster                                                            |
| scimark_fft             | 424 ms                                                 | 319 ms: 1.33x faster                                                             |
| deepcopy                | 442 us                                                 | 335 us: 1.32x faster                                                             |
| regex_compile           | 177 ms                                                 | 134 ms: 1.32x faster                                                             |
| fannkuch                | 486 ms                                                 | 371 ms: 1.31x faster                                                             |
| sqlglot_normalize       | 135 ms                                                 | 104 ms: 1.30x faster                                                             |
| thrift                  | 1.03 ms                                                | 796 us: 1.30x faster                                                             |
| async_tree_memoization  | 854 ms                                                 | 660 ms: 1.29x faster                                                             |
| deepcopy_reduce         | 3.82 us                                                | 2.96 us: 1.29x faster                                                            |
| sqlglot_optimize        | 65.3 ms                                                | 50.8 ms: 1.29x faster                                                            |
| async_tree_cpu_io_mixed | 951 ms                                                 | 745 ms: 1.28x faster                                                             |
| mypy2                   | 428 ms                                                 | 335 ms: 1.28x faster                                                             |
| docutils                | 3.17 sec                                               | 2.55 sec: 1.24x faster                                                           |
| nqueens                 | 100 ms                                                 | 81.1 ms: 1.23x faster                                                            |
| sqlalchemy_declarative  | 165 ms                                                 | 138 ms: 1.20x faster                                                             |
| bench_thread_pool       | 947 us                                                 | 793 us: 1.20x faster                                                             |
| dulwich_log             | 75.9 ms                                                | 63.8 ms: 1.19x faster                                                            |
| sympy_integrate         | 24.3 ms                                                | 20.5 ms: 1.18x faster                                                            |
| sympy_expand            | 545 ms                                                 | 462 ms: 1.18x faster                                                             |
| json_loads              | 28.8 us                                                | 24.4 us: 1.18x faster                                                            |
| sqlalchemy_imperative   | 21.2 ms                                                | 18.0 ms: 1.18x faster                                                            |
| json                    | 5.42 ms                                                | 4.64 ms: 1.17x faster                                                            |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.68 ms: 1.16x faster                                                            |
| xml_etree_generate      | 94.2 ms                                                | 81.0 ms: 1.16x faster                                                            |
| sympy_str               | 328 ms                                                 | 285 ms: 1.15x faster                                                             |
| regex_v8                | 25.0 ms                                                | 21.8 ms: 1.15x faster                                                            |
| comprehensions          | 26.8 us                                                | 23.8 us: 1.13x faster                                                            |
| pathlib                 | 20.0 ms                                                | 17.8 ms: 1.12x faster                                                            |
| xml_etree_iterparse     | 111 ms                                                 | 99.4 ms: 1.12x faster                                                            |
| create_gc_cycles        | 1.67 ms                                                | 1.50 ms: 1.12x faster                                                            |
| pickle_list             | 4.56 us                                                | 4.12 us: 1.11x faster                                                            |
| sqlite_synth            | 2.93 us                                                | 2.65 us: 1.11x faster                                                            |
| meteor_contest          | 115 ms                                                 | 104 ms: 1.11x faster                                                             |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.11x faster                                                             |
| sympy_sum               | 185 ms                                                 | 168 ms: 1.10x faster                                                             |
| djangocms               | 35.9 us                                                | 32.9 us: 1.09x faster                                                            |
| regex_dna               | 222 ms                                                 | 203 ms: 1.09x faster                                                             |
| mdp                     | 2.82 sec                                               | 2.63 sec: 1.07x faster                                                           |
| async_generators        | 425 ms                                                 | 413 ms: 1.03x faster                                                             |
| pickle                  | 10.3 us                                                | 10.2 us: 1.01x faster                                                            |
| pidigits                | 190 ms                                                 | 190 ms: 1.00x faster                                                             |
| bench_mp_pool           | 24.0 ms                                                | 24.0 ms: 1.00x slower                                                            |
| gc_traversal            | 3.84 ms                                                | 3.93 ms: 1.02x slower                                                            |
| regex_effbot            | 3.23 ms                                                | 3.36 ms: 1.04x slower                                                            |
| unpickle_list           | 4.82 us                                                | 5.05 us: 1.05x slower                                                            |
| python_startup_no_site  | 5.82 ms                                                | 6.54 ms: 1.12x slower                                                            |
| pickle_dict             | 27.3 us                                                | 31.1 us: 1.14x slower                                                            |
| dask                    | 423 ms                                                 | 509 ms: 1.20x slower                                                             |
| coverage                | 72.8 ms                                                | 93.6 ms: 1.29x slower                                                            |
| Geometric mean          | (ref)                                                  | 1.29x faster                                                                     |

Benchmark hidden because not significant (2): unpickle, telco
Ignored benchmarks (6) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.29x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.24x
