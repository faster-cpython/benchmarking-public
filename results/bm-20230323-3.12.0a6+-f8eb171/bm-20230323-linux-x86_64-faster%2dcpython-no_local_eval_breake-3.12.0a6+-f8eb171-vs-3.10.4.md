
# Results vs. 3.10.4

- fork: faster-cpython
- ref: no_local_eval_breake
- machine: linux-x86_64
- commit hash: f8eb171
- commit date: 2023-03-23
- overall geometric mean: 1.29x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230323-linux-x86_64-faster%2dcpython-no_local_eval_breake-3.12.0a6+-f8eb171 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 254 ms: 1.32x faster                                                             |
| chameleon      | 9.06 ms                                                | 6.44 ms: 1.41x faster                                                            |
| docutils       | 3.17 sec                                               | 2.54 sec: 1.25x faster                                                           |
| html5lib       | 85.9 ms                                                | 62.5 ms: 1.37x faster                                                            |
| tornado_http   | 127 ms                                                 | 91.1 ms: 1.40x faster                                                            |
| Geometric mean | (ref)                                                  | 1.35x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230323-linux-x86_64-faster%2dcpython-no_local_eval_breake-3.12.0a6+-f8eb171 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 87.6 ms: 1.62x faster                                                            |
| float          | 111 ms                                                 | 75.2 ms: 1.47x faster                                                            |
| pidigits       | 190 ms                                                 | 188 ms: 1.01x faster                                                             |
| Geometric mean | (ref)                                                  | 1.34x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230323-linux-x86_64-faster%2dcpython-no_local_eval_breake-3.12.0a6+-f8eb171 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 135 ms: 1.31x faster                                                             |
| regex_v8       | 25.0 ms                                                | 21.9 ms: 1.14x faster                                                            |
| regex_dna      | 222 ms                                                 | 207 ms: 1.07x faster                                                             |
| regex_effbot   | 3.23 ms                                                | 3.50 ms: 1.08x slower                                                            |
| Geometric mean | (ref)                                                  | 1.10x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230323-linux-x86_64-faster%2dcpython-no_local_eval_breake-3.12.0a6+-f8eb171 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 288 us: 1.58x faster                                                             |
| unpickle_pure_python | 300 us                                                 | 203 us: 1.48x faster                                                             |
| json_dumps           | 13.5 ms                                                | 9.61 ms: 1.41x faster                                                            |
| xml_etree_process    | 74.9 ms                                                | 56.5 ms: 1.33x faster                                                            |
| json_loads           | 28.8 us                                                | 24.1 us: 1.20x faster                                                            |
| xml_etree_generate   | 94.2 ms                                                | 81.8 ms: 1.15x faster                                                            |
| xml_etree_iterparse  | 111 ms                                                 | 100 ms: 1.11x faster                                                             |
| xml_etree_parse      | 163 ms                                                 | 149 ms: 1.10x faster                                                             |
| pickle_list          | 4.56 us                                                | 4.21 us: 1.08x faster                                                            |
| unpickle             | 14.1 us                                                | 13.6 us: 1.04x faster                                                            |
| unpickle_list        | 4.82 us                                                | 5.00 us: 1.04x slower                                                            |
| pickle_dict          | 27.3 us                                                | 31.1 us: 1.14x slower                                                            |
| Geometric mean       | (ref)                                                  | 1.16x faster                                                                     |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230323-linux-x86_64-faster%2dcpython-no_local_eval_breake-3.12.0a6+-f8eb171 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.84 ms: 1.60x faster                                                            |
| python_startup_no_site | 5.82 ms                                                | 6.53 ms: 1.12x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.19x faster                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230323-linux-x86_64-faster%2dcpython-no_local_eval_breake-3.12.0a6+-f8eb171 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.95 ms: 1.48x faster                                                            |
| genshi_text     | 30.3 ms                                                | 21.6 ms: 1.40x faster                                                            |
| django_template | 45.9 ms                                                | 33.6 ms: 1.37x faster                                                            |
| genshi_xml      | 63.3 ms                                                | 48.2 ms: 1.31x faster                                                            |
| Geometric mean  | (ref)                                                  | 1.39x faster                                                                     |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230323-linux-x86_64-faster%2dcpython-no_local_eval_breake-3.12.0a6+-f8eb171 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| generators              | 76.8 ms                                                | 29.3 ms: 2.62x faster                                                            |
| deltablue               | 7.42 ms                                                | 3.26 ms: 2.27x faster                                                            |
| asyncio_tcp             | 925 ms                                                 | 506 ms: 1.83x faster                                                             |
| logging_silent          | 175 ns                                                 | 98.2 ns: 1.78x faster                                                            |
| scimark_sor             | 197 ms                                                 | 112 ms: 1.75x faster                                                             |
| go                      | 229 ms                                                 | 137 ms: 1.68x faster                                                             |
| richards                | 74.9 ms                                                | 44.7 ms: 1.68x faster                                                            |
| spectral_norm           | 150 ms                                                 | 92.1 ms: 1.63x faster                                                            |
| raytrace                | 464 ms                                                 | 285 ms: 1.63x faster                                                             |
| nbody                   | 142 ms                                                 | 87.6 ms: 1.62x faster                                                            |
| scimark_monte_carlo     | 108 ms                                                 | 67.1 ms: 1.61x faster                                                            |
| chaos                   | 106 ms                                                 | 66.1 ms: 1.61x faster                                                            |
| python_startup          | 14.2 ms                                                | 8.84 ms: 1.60x faster                                                            |
| pyflate                 | 673 ms                                                 | 423 ms: 1.59x faster                                                             |
| crypto_pyaes            | 118 ms                                                 | 74.8 ms: 1.58x faster                                                            |
| pickle_pure_python      | 455 us                                                 | 288 us: 1.58x faster                                                             |
| hexiom                  | 9.53 ms                                                | 6.14 ms: 1.55x faster                                                            |
| deepcopy_memo           | 52.3 us                                                | 34.8 us: 1.51x faster                                                            |
| mako                    | 14.8 ms                                                | 9.95 ms: 1.48x faster                                                            |
| unpickle_pure_python    | 300 us                                                 | 203 us: 1.48x faster                                                             |
| scimark_lu              | 163 ms                                                 | 110 ms: 1.48x faster                                                             |
| float                   | 111 ms                                                 | 75.2 ms: 1.47x faster                                                            |
| sqlglot_parse           | 2.06 ms                                                | 1.43 ms: 1.44x faster                                                            |
| sqlglot_transpile       | 2.45 ms                                                | 1.72 ms: 1.42x faster                                                            |
| pprint_pformat          | 1.99 sec                                               | 1.40 sec: 1.41x faster                                                           |
| logging_format          | 8.91 us                                                | 6.30 us: 1.41x faster                                                            |
| logging_simple          | 8.07 us                                                | 5.71 us: 1.41x faster                                                            |
| json_dumps              | 13.5 ms                                                | 9.61 ms: 1.41x faster                                                            |
| chameleon               | 9.06 ms                                                | 6.44 ms: 1.41x faster                                                            |
| genshi_text             | 30.3 ms                                                | 21.6 ms: 1.40x faster                                                            |
| tornado_http            | 127 ms                                                 | 91.1 ms: 1.40x faster                                                            |
| pprint_safe_repr        | 955 ms                                                 | 683 ms: 1.40x faster                                                             |
| unpack_sequence         | 64.7 ns                                                | 46.5 ns: 1.39x faster                                                            |
| scimark_fft             | 424 ms                                                 | 307 ms: 1.38x faster                                                             |
| coroutines              | 31.8 ms                                                | 23.1 ms: 1.38x faster                                                            |
| html5lib                | 85.9 ms                                                | 62.5 ms: 1.37x faster                                                            |
| aiohttp                 | 1.38 ms                                                | 1.01 ms: 1.37x faster                                                            |
| async_tree_none         | 717 ms                                                 | 523 ms: 1.37x faster                                                             |
| django_template         | 45.9 ms                                                | 33.6 ms: 1.37x faster                                                            |
| async_tree_io           | 1.77 sec                                               | 1.30 sec: 1.36x faster                                                           |
| gunicorn                | 1.46 ms                                                | 1.09 ms: 1.34x faster                                                            |
| pycparser               | 1.50 sec                                               | 1.12 sec: 1.34x faster                                                           |
| deepcopy                | 442 us                                                 | 333 us: 1.33x faster                                                             |
| xml_etree_process       | 74.9 ms                                                | 56.5 ms: 1.33x faster                                                            |
| 2to3                    | 336 ms                                                 | 254 ms: 1.32x faster                                                             |
| thrift                  | 1.03 ms                                                | 786 us: 1.32x faster                                                             |
| genshi_xml              | 63.3 ms                                                | 48.2 ms: 1.31x faster                                                            |
| fannkuch                | 486 ms                                                 | 370 ms: 1.31x faster                                                             |
| regex_compile           | 177 ms                                                 | 135 ms: 1.31x faster                                                             |
| async_tree_memoization  | 854 ms                                                 | 656 ms: 1.30x faster                                                             |
| mypy2                   | 428 ms                                                 | 334 ms: 1.28x faster                                                             |
| async_tree_cpu_io_mixed | 951 ms                                                 | 743 ms: 1.28x faster                                                             |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.28 ms: 1.27x faster                                                            |
| sqlglot_normalize       | 135 ms                                                 | 106 ms: 1.27x faster                                                             |
| sqlglot_optimize        | 65.3 ms                                                | 51.5 ms: 1.27x faster                                                            |
| deepcopy_reduce         | 3.82 us                                                | 3.02 us: 1.27x faster                                                            |
| docutils                | 3.17 sec                                               | 2.54 sec: 1.25x faster                                                           |
| nqueens                 | 100 ms                                                 | 80.6 ms: 1.24x faster                                                            |
| sqlalchemy_declarative  | 165 ms                                                 | 137 ms: 1.20x faster                                                             |
| dulwich_log             | 75.9 ms                                                | 63.3 ms: 1.20x faster                                                            |
| bench_thread_pool       | 947 us                                                 | 791 us: 1.20x faster                                                             |
| json_loads              | 28.8 us                                                | 24.1 us: 1.20x faster                                                            |
| sqlalchemy_imperative   | 21.2 ms                                                | 17.8 ms: 1.19x faster                                                            |
| sympy_expand            | 545 ms                                                 | 460 ms: 1.18x faster                                                             |
| sympy_integrate         | 24.3 ms                                                | 20.5 ms: 1.18x faster                                                            |
| json                    | 5.42 ms                                                | 4.63 ms: 1.17x faster                                                            |
| sympy_str               | 328 ms                                                 | 285 ms: 1.15x faster                                                             |
| xml_etree_generate      | 94.2 ms                                                | 81.8 ms: 1.15x faster                                                            |
| regex_v8                | 25.0 ms                                                | 21.9 ms: 1.14x faster                                                            |
| comprehensions          | 26.8 us                                                | 23.5 us: 1.14x faster                                                            |
| sqlite_synth            | 2.93 us                                                | 2.61 us: 1.12x faster                                                            |
| create_gc_cycles        | 1.67 ms                                                | 1.49 ms: 1.12x faster                                                            |
| mdp                     | 2.82 sec                                               | 2.52 sec: 1.12x faster                                                           |
| djangocms               | 35.9 us                                                | 32.2 us: 1.12x faster                                                            |
| sympy_sum               | 185 ms                                                 | 166 ms: 1.11x faster                                                             |
| xml_etree_iterparse     | 111 ms                                                 | 100 ms: 1.11x faster                                                             |
| meteor_contest          | 115 ms                                                 | 104 ms: 1.11x faster                                                             |
| pathlib                 | 20.0 ms                                                | 18.1 ms: 1.11x faster                                                            |
| xml_etree_parse         | 163 ms                                                 | 149 ms: 1.10x faster                                                             |
| pickle_list             | 4.56 us                                                | 4.21 us: 1.08x faster                                                            |
| regex_dna               | 222 ms                                                 | 207 ms: 1.07x faster                                                             |
| async_generators        | 425 ms                                                 | 407 ms: 1.05x faster                                                             |
| unpickle                | 14.1 us                                                | 13.6 us: 1.04x faster                                                            |
| telco                   | 6.54 ms                                                | 6.39 ms: 1.02x faster                                                            |
| pidigits                | 190 ms                                                 | 188 ms: 1.01x faster                                                             |
| gc_traversal            | 3.84 ms                                                | 3.82 ms: 1.01x faster                                                            |
| unpickle_list           | 4.82 us                                                | 5.00 us: 1.04x slower                                                            |
| regex_effbot            | 3.23 ms                                                | 3.50 ms: 1.08x slower                                                            |
| python_startup_no_site  | 5.82 ms                                                | 6.53 ms: 1.12x slower                                                            |
| pickle_dict             | 27.3 us                                                | 31.1 us: 1.14x slower                                                            |
| dask                    | 423 ms                                                 | 512 ms: 1.21x slower                                                             |
| coverage                | 72.8 ms                                                | 97.5 ms: 1.34x slower                                                            |
| Geometric mean          | (ref)                                                  | 1.29x faster                                                                     |

Benchmark hidden because not significant (2): bench_mp_pool, pickle
Ignored benchmarks (6) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.29x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.24x
