
# Results vs. 3.10.4

- fork: faster-cpython
- ref: allow_non_python_fra
- machine: linux-x86_64
- commit hash: 3e2c3ab
- commit date: 2023-03-15
- overall geometric mean: 1.29x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230315-linux-x86_64-faster%2dcpython-allow_non_python_fra-3.12.0a6+-3e2c3ab |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 252 ms: 1.33x faster                                                             |
| chameleon      | 9.17 ms                                                | 6.42 ms: 1.43x faster                                                            |
| docutils       | 3.18 sec                                               | 2.55 sec: 1.25x faster                                                           |
| html5lib       | 85.9 ms                                                | 62.1 ms: 1.38x faster                                                            |
| tornado_http   | 128 ms                                                 | 95.2 ms: 1.35x faster                                                            |
| Geometric mean | (ref)                                                  | 1.35x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230315-linux-x86_64-faster%2dcpython-allow_non_python_fra-3.12.0a6+-3e2c3ab |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 144 ms                                                 | 95.6 ms: 1.51x faster                                                            |
| float          | 109 ms                                                 | 75.2 ms: 1.45x faster                                                            |
| pidigits       | 190 ms                                                 | 190 ms: 1.00x faster                                                             |
| Geometric mean | (ref)                                                  | 1.30x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230315-linux-x86_64-faster%2dcpython-allow_non_python_fra-3.12.0a6+-3e2c3ab |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 134 ms: 1.32x faster                                                             |
| regex_v8       | 25.0 ms                                                | 21.8 ms: 1.15x faster                                                            |
| regex_dna      | 214 ms                                                 | 203 ms: 1.05x faster                                                             |
| regex_effbot   | 3.19 ms                                                | 3.36 ms: 1.05x slower                                                            |
| Geometric mean | (ref)                                                  | 1.11x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230315-linux-x86_64-faster%2dcpython-allow_non_python_fra-3.12.0a6+-3e2c3ab |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 286 us: 1.58x faster                                                             |
| unpickle_pure_python | 302 us                                                 | 201 us: 1.50x faster                                                             |
| json_dumps           | 13.4 ms                                                | 9.55 ms: 1.41x faster                                                            |
| xml_etree_process    | 74.5 ms                                                | 55.2 ms: 1.35x faster                                                            |
| json_loads           | 28.7 us                                                | 24.4 us: 1.17x faster                                                            |
| xml_etree_generate   | 93.8 ms                                                | 81.0 ms: 1.16x faster                                                            |
| pickle_list          | 4.72 us                                                | 4.12 us: 1.15x faster                                                            |
| xml_etree_iterparse  | 111 ms                                                 | 99.4 ms: 1.12x faster                                                            |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.10x faster                                                             |
| unpickle_list        | 4.92 us                                                | 5.05 us: 1.03x slower                                                            |
| pickle_dict          | 27.6 us                                                | 31.1 us: 1.13x slower                                                            |
| Geometric mean       | (ref)                                                  | 1.17x faster                                                                     |

Benchmark hidden because not significant (2): unpickle, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230315-linux-x86_64-faster%2dcpython-allow_non_python_fra-3.12.0a6+-3e2c3ab |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 9.02 ms: 1.56x faster                                                            |
| python_startup_no_site | 5.78 ms                                                | 6.54 ms: 1.13x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.17x faster                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230315-linux-x86_64-faster%2dcpython-allow_non_python_fra-3.12.0a6+-3e2c3ab |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                | 10.0 ms: 1.46x faster                                                            |
| genshi_text     | 30.6 ms                                                | 21.5 ms: 1.43x faster                                                            |
| django_template | 46.3 ms                                                | 33.5 ms: 1.38x faster                                                            |
| genshi_xml      | 63.7 ms                                                | 47.7 ms: 1.34x faster                                                            |
| Geometric mean  | (ref)                                                  | 1.40x faster                                                                     |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230315-linux-x86_64-faster%2dcpython-allow_non_python_fra-3.12.0a6+-3e2c3ab |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| generators              | 76.4 ms                                                | 29.3 ms: 2.61x faster                                                            |
| deltablue               | 7.28 ms                                                | 3.21 ms: 2.27x faster                                                            |
| scimark_sor             | 197 ms                                                 | 107 ms: 1.85x faster                                                             |
| logging_silent          | 176 ns                                                 | 96.1 ns: 1.84x faster                                                            |
| asyncio_tcp             | 914 ms                                                 | 515 ms: 1.77x faster                                                             |
| richards                | 75.2 ms                                                | 44.0 ms: 1.71x faster                                                            |
| pyflate                 | 676 ms                                                 | 409 ms: 1.65x faster                                                             |
| go                      | 226 ms                                                 | 137 ms: 1.65x faster                                                             |
| raytrace                | 467 ms                                                 | 287 ms: 1.63x faster                                                             |
| scimark_monte_carlo     | 109 ms                                                 | 67.8 ms: 1.60x faster                                                            |
| pickle_pure_python      | 452 us                                                 | 286 us: 1.58x faster                                                             |
| crypto_pyaes            | 117 ms                                                 | 74.2 ms: 1.57x faster                                                            |
| python_startup          | 14.1 ms                                                | 9.02 ms: 1.56x faster                                                            |
| chaos                   | 106 ms                                                 | 67.9 ms: 1.56x faster                                                            |
| spectral_norm           | 150 ms                                                 | 97.8 ms: 1.53x faster                                                            |
| nbody                   | 144 ms                                                 | 95.6 ms: 1.51x faster                                                            |
| hexiom                  | 9.43 ms                                                | 6.27 ms: 1.50x faster                                                            |
| deepcopy_memo           | 51.7 us                                                | 34.4 us: 1.50x faster                                                            |
| unpickle_pure_python    | 302 us                                                 | 201 us: 1.50x faster                                                             |
| mako                    | 14.7 ms                                                | 10.0 ms: 1.46x faster                                                            |
| float                   | 109 ms                                                 | 75.2 ms: 1.45x faster                                                            |
| scimark_lu              | 161 ms                                                 | 112 ms: 1.44x faster                                                             |
| genshi_text             | 30.6 ms                                                | 21.5 ms: 1.43x faster                                                            |
| chameleon               | 9.17 ms                                                | 6.42 ms: 1.43x faster                                                            |
| sqlglot_parse           | 2.04 ms                                                | 1.44 ms: 1.42x faster                                                            |
| pprint_pformat          | 1.98 sec                                               | 1.39 sec: 1.42x faster                                                           |
| sqlglot_transpile       | 2.43 ms                                                | 1.72 ms: 1.41x faster                                                            |
| json_dumps              | 13.4 ms                                                | 9.55 ms: 1.41x faster                                                            |
| pprint_safe_repr        | 953 ms                                                 | 683 ms: 1.40x faster                                                             |
| coroutines              | 31.6 ms                                                | 22.9 ms: 1.38x faster                                                            |
| django_template         | 46.3 ms                                                | 33.5 ms: 1.38x faster                                                            |
| html5lib                | 85.9 ms                                                | 62.1 ms: 1.38x faster                                                            |
| logging_simple          | 8.10 us                                                | 5.86 us: 1.38x faster                                                            |
| logging_format          | 8.85 us                                                | 6.41 us: 1.38x faster                                                            |
| async_tree_io           | 1.78 sec                                               | 1.30 sec: 1.37x faster                                                           |
| unpack_sequence         | 59.4 ns                                                | 43.8 ns: 1.36x faster                                                            |
| pycparser               | 1.53 sec                                               | 1.13 sec: 1.35x faster                                                           |
| async_tree_none         | 711 ms                                                 | 526 ms: 1.35x faster                                                             |
| xml_etree_process       | 74.5 ms                                                | 55.2 ms: 1.35x faster                                                            |
| tornado_http            | 128 ms                                                 | 95.2 ms: 1.35x faster                                                            |
| genshi_xml              | 63.7 ms                                                | 47.7 ms: 1.34x faster                                                            |
| 2to3                    | 335 ms                                                 | 252 ms: 1.33x faster                                                             |
| aiohttp                 | 1.34 ms                                                | 1.01 ms: 1.33x faster                                                            |
| regex_compile           | 177 ms                                                 | 134 ms: 1.32x faster                                                             |
| scimark_fft             | 421 ms                                                 | 319 ms: 1.32x faster                                                             |
| fannkuch                | 488 ms                                                 | 371 ms: 1.31x faster                                                             |
| deepcopy                | 438 us                                                 | 335 us: 1.31x faster                                                             |
| gunicorn                | 1.43 ms                                                | 1.10 ms: 1.30x faster                                                            |
| thrift                  | 1.03 ms                                                | 796 us: 1.30x faster                                                             |
| async_tree_memoization  | 855 ms                                                 | 660 ms: 1.29x faster                                                             |
| sqlglot_normalize       | 134 ms                                                 | 104 ms: 1.29x faster                                                             |
| sqlglot_optimize        | 65.2 ms                                                | 50.8 ms: 1.28x faster                                                            |
| mypy2                   | 430 ms                                                 | 335 ms: 1.28x faster                                                             |
| deepcopy_reduce         | 3.79 us                                                | 2.96 us: 1.28x faster                                                            |
| async_tree_cpu_io_mixed | 949 ms                                                 | 745 ms: 1.27x faster                                                             |
| docutils                | 3.18 sec                                               | 2.55 sec: 1.25x faster                                                           |
| nqueens                 | 100 ms                                                 | 81.1 ms: 1.23x faster                                                            |
| sqlalchemy_declarative  | 165 ms                                                 | 138 ms: 1.20x faster                                                             |
| bench_thread_pool       | 946 us                                                 | 793 us: 1.19x faster                                                             |
| sqlalchemy_imperative   | 21.5 ms                                                | 18.0 ms: 1.19x faster                                                            |
| dulwich_log             | 75.8 ms                                                | 63.8 ms: 1.19x faster                                                            |
| json_loads              | 28.7 us                                                | 24.4 us: 1.17x faster                                                            |
| sympy_integrate         | 24.0 ms                                                | 20.5 ms: 1.17x faster                                                            |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.68 ms: 1.16x faster                                                            |
| xml_etree_generate      | 93.8 ms                                                | 81.0 ms: 1.16x faster                                                            |
| sympy_expand            | 534 ms                                                 | 462 ms: 1.15x faster                                                             |
| json                    | 5.35 ms                                                | 4.64 ms: 1.15x faster                                                            |
| regex_v8                | 25.0 ms                                                | 21.8 ms: 1.15x faster                                                            |
| pickle_list             | 4.72 us                                                | 4.12 us: 1.15x faster                                                            |
| sympy_str               | 325 ms                                                 | 285 ms: 1.14x faster                                                             |
| pathlib                 | 20.0 ms                                                | 17.8 ms: 1.12x faster                                                            |
| djangocms               | 36.9 us                                                | 32.9 us: 1.12x faster                                                            |
| xml_etree_iterparse     | 111 ms                                                 | 99.4 ms: 1.12x faster                                                            |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.10x faster                                                             |
| sqlite_synth            | 2.92 us                                                | 2.65 us: 1.10x faster                                                            |
| create_gc_cycles        | 1.65 ms                                                | 1.50 ms: 1.10x faster                                                            |
| meteor_contest          | 114 ms                                                 | 104 ms: 1.10x faster                                                             |
| sympy_sum               | 183 ms                                                 | 168 ms: 1.09x faster                                                             |
| regex_dna               | 214 ms                                                 | 203 ms: 1.05x faster                                                             |
| mdp                     | 2.74 sec                                               | 2.63 sec: 1.04x faster                                                           |
| async_generators        | 426 ms                                                 | 413 ms: 1.03x faster                                                             |
| telco                   | 6.73 ms                                                | 6.52 ms: 1.03x faster                                                            |
| pidigits                | 190 ms                                                 | 190 ms: 1.00x faster                                                             |
| unpickle_list           | 4.92 us                                                | 5.05 us: 1.03x slower                                                            |
| regex_effbot            | 3.19 ms                                                | 3.36 ms: 1.05x slower                                                            |
| gc_traversal            | 3.53 ms                                                | 3.93 ms: 1.11x slower                                                            |
| pickle_dict             | 27.6 us                                                | 31.1 us: 1.13x slower                                                            |
| python_startup_no_site  | 5.78 ms                                                | 6.54 ms: 1.13x slower                                                            |
| dask                    | 436 ms                                                 | 509 ms: 1.17x slower                                                             |
| coverage                | 74.7 ms                                                | 93.6 ms: 1.25x slower                                                            |
| Geometric mean          | (ref)                                                  | 1.29x faster                                                                     |

Benchmark hidden because not significant (3): unpickle, bench_mp_pool, pickle
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, pylint
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230315-3.12.0a6+-3e2c3ab/bm-20230315-linux-x86_64-faster%2dcpython-allow_non_python_fra-3.12.0a6+-3e2c3ab.json: comprehensions
