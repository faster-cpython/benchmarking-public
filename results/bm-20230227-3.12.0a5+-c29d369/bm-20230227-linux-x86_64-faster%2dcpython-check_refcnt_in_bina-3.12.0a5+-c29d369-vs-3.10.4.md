
# Results vs. 3.10.4

- fork: faster-cpython
- ref: check_refcnt_in_bina
- machine: linux-x86_64
- commit hash: c29d369
- commit date: 2023-02-27
- overall geometric mean: 1.31x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230227-linux-x86_64-faster%2dcpython-check_refcnt_in_bina-3.12.0a5+-c29d369 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 248 ms: 1.35x faster                                                             |
| chameleon      | 9.17 ms                                                | 6.51 ms: 1.41x faster                                                            |
| docutils       | 3.18 sec                                               | 2.53 sec: 1.25x faster                                                           |
| html5lib       | 85.9 ms                                                | 61.4 ms: 1.40x faster                                                            |
| tornado_http   | 128 ms                                                 | 94.3 ms: 1.36x faster                                                            |
| Geometric mean | (ref)                                                  | 1.35x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230227-linux-x86_64-faster%2dcpython-check_refcnt_in_bina-3.12.0a5+-c29d369 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 144 ms                                                 | 89.7 ms: 1.60x faster                                                            |
| float          | 109 ms                                                 | 72.2 ms: 1.51x faster                                                            |
| pidigits       | 190 ms                                                 | 197 ms: 1.04x slower                                                             |
| Geometric mean | (ref)                                                  | 1.33x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230227-linux-x86_64-faster%2dcpython-check_refcnt_in_bina-3.12.0a5+-c29d369 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 132 ms: 1.34x faster                                                             |
| regex_v8       | 25.0 ms                                                | 22.2 ms: 1.13x faster                                                            |
| regex_dna      | 214 ms                                                 | 209 ms: 1.02x faster                                                             |
| regex_effbot   | 3.19 ms                                                | 3.36 ms: 1.05x slower                                                            |
| Geometric mean | (ref)                                                  | 1.10x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230227-linux-x86_64-faster%2dcpython-check_refcnt_in_bina-3.12.0a5+-c29d369 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 284 us: 1.59x faster                                                             |
| unpickle_pure_python | 302 us                                                 | 196 us: 1.54x faster                                                             |
| json_dumps           | 13.4 ms                                                | 9.62 ms: 1.40x faster                                                            |
| xml_etree_process    | 74.5 ms                                                | 54.9 ms: 1.36x faster                                                            |
| json_loads           | 28.7 us                                                | 24.0 us: 1.20x faster                                                            |
| xml_etree_generate   | 93.8 ms                                                | 79.7 ms: 1.18x faster                                                            |
| pickle_list          | 4.72 us                                                | 4.12 us: 1.15x faster                                                            |
| xml_etree_iterparse  | 111 ms                                                 | 98.7 ms: 1.12x faster                                                            |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.10x faster                                                             |
| unpickle             | 14.2 us                                                | 13.3 us: 1.06x faster                                                            |
| pickle               | 10.2 us                                                | 10.3 us: 1.01x slower                                                            |
| pickle_dict          | 27.6 us                                                | 30.7 us: 1.11x slower                                                            |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                                     |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230227-linux-x86_64-faster%2dcpython-check_refcnt_in_bina-3.12.0a5+-c29d369 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.98 ms: 1.57x faster                                                            |
| python_startup_no_site | 5.78 ms                                                | 6.51 ms: 1.13x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.18x faster                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230227-linux-x86_64-faster%2dcpython-check_refcnt_in_bina-3.12.0a5+-c29d369 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                | 9.92 ms: 1.48x faster                                                            |
| genshi_text     | 30.6 ms                                                | 20.9 ms: 1.46x faster                                                            |
| django_template | 46.3 ms                                                | 33.1 ms: 1.40x faster                                                            |
| genshi_xml      | 63.7 ms                                                | 46.8 ms: 1.36x faster                                                            |
| Geometric mean  | (ref)                                                  | 1.42x faster                                                                     |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230227-linux-x86_64-faster%2dcpython-check_refcnt_in_bina-3.12.0a5+-c29d369 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| generators              | 76.4 ms                                                | 29.7 ms: 2.57x faster                                                            |
| deltablue               | 7.28 ms                                                | 3.11 ms: 2.34x faster                                                            |
| scimark_sor             | 197 ms                                                 | 103 ms: 1.91x faster                                                             |
| logging_silent          | 176 ns                                                 | 92.6 ns: 1.91x faster                                                            |
| richards                | 75.2 ms                                                | 40.9 ms: 1.84x faster                                                            |
| asyncio_tcp             | 914 ms                                                 | 503 ms: 1.82x faster                                                             |
| spectral_norm           | 150 ms                                                 | 87.7 ms: 1.71x faster                                                            |
| go                      | 226 ms                                                 | 134 ms: 1.68x faster                                                             |
| raytrace                | 467 ms                                                 | 278 ms: 1.68x faster                                                             |
| pyflate                 | 676 ms                                                 | 407 ms: 1.66x faster                                                             |
| nbody                   | 144 ms                                                 | 89.7 ms: 1.60x faster                                                            |
| scimark_monte_carlo     | 109 ms                                                 | 68.0 ms: 1.60x faster                                                            |
| pickle_pure_python      | 452 us                                                 | 284 us: 1.59x faster                                                             |
| crypto_pyaes            | 117 ms                                                 | 73.5 ms: 1.59x faster                                                            |
| python_startup          | 14.1 ms                                                | 8.98 ms: 1.57x faster                                                            |
| hexiom                  | 9.43 ms                                                | 6.08 ms: 1.55x faster                                                            |
| chaos                   | 106 ms                                                 | 68.4 ms: 1.54x faster                                                            |
| unpickle_pure_python    | 302 us                                                 | 196 us: 1.54x faster                                                             |
| float                   | 109 ms                                                 | 72.2 ms: 1.51x faster                                                            |
| deepcopy_memo           | 51.7 us                                                | 34.4 us: 1.50x faster                                                            |
| scimark_lu              | 161 ms                                                 | 108 ms: 1.49x faster                                                             |
| mako                    | 14.7 ms                                                | 9.92 ms: 1.48x faster                                                            |
| genshi_text             | 30.6 ms                                                | 20.9 ms: 1.46x faster                                                            |
| sqlglot_parse           | 2.04 ms                                                | 1.41 ms: 1.44x faster                                                            |
| sqlglot_transpile       | 2.43 ms                                                | 1.71 ms: 1.42x faster                                                            |
| pprint_pformat          | 1.98 sec                                               | 1.41 sec: 1.41x faster                                                           |
| chameleon               | 9.17 ms                                                | 6.51 ms: 1.41x faster                                                            |
| scimark_fft             | 421 ms                                                 | 300 ms: 1.40x faster                                                             |
| async_tree_io           | 1.78 sec                                               | 1.27 sec: 1.40x faster                                                           |
| django_template         | 46.3 ms                                                | 33.1 ms: 1.40x faster                                                            |
| html5lib                | 85.9 ms                                                | 61.4 ms: 1.40x faster                                                            |
| pycparser               | 1.53 sec                                               | 1.10 sec: 1.40x faster                                                           |
| json_dumps              | 13.4 ms                                                | 9.62 ms: 1.40x faster                                                            |
| logging_format          | 8.85 us                                                | 6.34 us: 1.40x faster                                                            |
| logging_simple          | 8.10 us                                                | 5.81 us: 1.40x faster                                                            |
| coroutines              | 31.6 ms                                                | 22.7 ms: 1.39x faster                                                            |
| pprint_safe_repr        | 953 ms                                                 | 685 ms: 1.39x faster                                                             |
| thrift                  | 1.03 ms                                                | 756 us: 1.37x faster                                                             |
| async_tree_none         | 711 ms                                                 | 521 ms: 1.36x faster                                                             |
| genshi_xml              | 63.7 ms                                                | 46.8 ms: 1.36x faster                                                            |
| tornado_http            | 128 ms                                                 | 94.3 ms: 1.36x faster                                                            |
| xml_etree_process       | 74.5 ms                                                | 54.9 ms: 1.36x faster                                                            |
| 2to3                    | 335 ms                                                 | 248 ms: 1.35x faster                                                             |
| fannkuch                | 488 ms                                                 | 361 ms: 1.35x faster                                                             |
| regex_compile           | 177 ms                                                 | 132 ms: 1.34x faster                                                             |
| unpack_sequence         | 59.4 ns                                                | 44.3 ns: 1.34x faster                                                            |
| aiohttp                 | 1.34 ms                                                | 1.01 ms: 1.33x faster                                                            |
| async_tree_memoization  | 855 ms                                                 | 645 ms: 1.32x faster                                                             |
| gunicorn                | 1.43 ms                                                | 1.09 ms: 1.32x faster                                                            |
| deepcopy                | 438 us                                                 | 333 us: 1.32x faster                                                             |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.17 ms: 1.31x faster                                                            |
| sqlglot_normalize       | 134 ms                                                 | 103 ms: 1.30x faster                                                             |
| mypy2                   | 430 ms                                                 | 331 ms: 1.30x faster                                                             |
| async_tree_cpu_io_mixed | 949 ms                                                 | 732 ms: 1.30x faster                                                             |
| sqlglot_optimize        | 65.2 ms                                                | 50.5 ms: 1.29x faster                                                            |
| deepcopy_reduce         | 3.79 us                                                | 2.97 us: 1.28x faster                                                            |
| nqueens                 | 100 ms                                                 | 78.6 ms: 1.27x faster                                                            |
| docutils                | 3.18 sec                                               | 2.53 sec: 1.25x faster                                                           |
| bench_thread_pool       | 946 us                                                 | 784 us: 1.21x faster                                                             |
| dulwich_log             | 75.8 ms                                                | 63.2 ms: 1.20x faster                                                            |
| json_loads              | 28.7 us                                                | 24.0 us: 1.20x faster                                                            |
| sqlalchemy_imperative   | 21.5 ms                                                | 18.0 ms: 1.19x faster                                                            |
| sqlalchemy_declarative  | 165 ms                                                 | 139 ms: 1.19x faster                                                             |
| xml_etree_generate      | 93.8 ms                                                | 79.7 ms: 1.18x faster                                                            |
| sympy_integrate         | 24.0 ms                                                | 20.5 ms: 1.17x faster                                                            |
| sympy_expand            | 534 ms                                                 | 457 ms: 1.17x faster                                                             |
| json                    | 5.35 ms                                                | 4.57 ms: 1.17x faster                                                            |
| sympy_str               | 325 ms                                                 | 283 ms: 1.15x faster                                                             |
| pickle_list             | 4.72 us                                                | 4.12 us: 1.15x faster                                                            |
| djangocms               | 36.9 us                                                | 32.3 us: 1.14x faster                                                            |
| pathlib                 | 20.0 ms                                                | 17.7 ms: 1.13x faster                                                            |
| regex_v8                | 25.0 ms                                                | 22.2 ms: 1.13x faster                                                            |
| xml_etree_iterparse     | 111 ms                                                 | 98.7 ms: 1.12x faster                                                            |
| sqlite_synth            | 2.92 us                                                | 2.61 us: 1.12x faster                                                            |
| create_gc_cycles        | 1.65 ms                                                | 1.47 ms: 1.12x faster                                                            |
| meteor_contest          | 114 ms                                                 | 102 ms: 1.11x faster                                                             |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.10x faster                                                             |
| sympy_sum               | 183 ms                                                 | 167 ms: 1.10x faster                                                             |
| unpickle                | 14.2 us                                                | 13.3 us: 1.06x faster                                                            |
| mdp                     | 2.74 sec                                               | 2.61 sec: 1.05x faster                                                           |
| async_generators        | 426 ms                                                 | 410 ms: 1.04x faster                                                             |
| telco                   | 6.73 ms                                                | 6.53 ms: 1.03x faster                                                            |
| regex_dna               | 214 ms                                                 | 209 ms: 1.02x faster                                                             |
| pickle                  | 10.2 us                                                | 10.3 us: 1.01x slower                                                            |
| pidigits                | 190 ms                                                 | 197 ms: 1.04x slower                                                             |
| regex_effbot            | 3.19 ms                                                | 3.36 ms: 1.05x slower                                                            |
| gc_traversal            | 3.53 ms                                                | 3.83 ms: 1.09x slower                                                            |
| pickle_dict             | 27.6 us                                                | 30.7 us: 1.11x slower                                                            |
| python_startup_no_site  | 5.78 ms                                                | 6.51 ms: 1.13x slower                                                            |
| dask                    | 436 ms                                                 | 498 ms: 1.14x slower                                                             |
| coverage                | 74.7 ms                                                | 97.5 ms: 1.30x slower                                                            |
| Geometric mean          | (ref)                                                  | 1.31x faster                                                                     |

Benchmark hidden because not significant (2): bench_mp_pool, unpickle_list
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, pylint
