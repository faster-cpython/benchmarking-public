
# Results vs. 3.10.4

- fork: iritkatriel
- ref: remove_JUMP_IF_FALSE
- machine: linux-x86_64
- commit hash: 12595f6
- commit date: 2023-03-21
- overall geometric mean: 1.30x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230321-linux-x86_64-iritkatriel-remove_JUMP_IF_FALSE-3.12.0a6+-12595f6 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 249 ms: 1.35x faster                                                        |
| chameleon      | 9.17 ms                                                | 6.56 ms: 1.40x faster                                                       |
| docutils       | 3.18 sec                                               | 2.54 sec: 1.25x faster                                                      |
| html5lib       | 85.9 ms                                                | 60.8 ms: 1.41x faster                                                       |
| tornado_http   | 128 ms                                                 | 91.5 ms: 1.40x faster                                                       |
| Geometric mean | (ref)                                                  | 1.36x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230321-linux-x86_64-iritkatriel-remove_JUMP_IF_FALSE-3.12.0a6+-12595f6 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 144 ms                                                 | 87.2 ms: 1.65x faster                                                       |
| float          | 109 ms                                                 | 73.2 ms: 1.49x faster                                                       |
| pidigits       | 190 ms                                                 | 189 ms: 1.00x faster                                                        |
| Geometric mean | (ref)                                                  | 1.35x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230321-linux-x86_64-iritkatriel-remove_JUMP_IF_FALSE-3.12.0a6+-12595f6 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 134 ms: 1.33x faster                                                        |
| regex_v8       | 25.0 ms                                                | 22.0 ms: 1.14x faster                                                       |
| regex_dna      | 214 ms                                                 | 201 ms: 1.06x faster                                                        |
| regex_effbot   | 3.19 ms                                                | 3.59 ms: 1.12x slower                                                       |
| Geometric mean | (ref)                                                  | 1.09x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230321-linux-x86_64-iritkatriel-remove_JUMP_IF_FALSE-3.12.0a6+-12595f6 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 287 us: 1.58x faster                                                        |
| unpickle_pure_python | 302 us                                                 | 198 us: 1.52x faster                                                        |
| json_dumps           | 13.4 ms                                                | 9.51 ms: 1.41x faster                                                       |
| xml_etree_process    | 74.5 ms                                                | 56.8 ms: 1.31x faster                                                       |
| json_loads           | 28.7 us                                                | 24.0 us: 1.19x faster                                                       |
| pickle_list          | 4.72 us                                                | 4.08 us: 1.16x faster                                                       |
| xml_etree_generate   | 93.8 ms                                                | 81.6 ms: 1.15x faster                                                       |
| xml_etree_parse      | 163 ms                                                 | 150 ms: 1.09x faster                                                        |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.08x faster                                                        |
| unpickle_list        | 4.92 us                                                | 5.01 us: 1.02x slower                                                       |
| pickle_dict          | 27.6 us                                                | 30.8 us: 1.12x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.17x faster                                                                |

Benchmark hidden because not significant (2): unpickle, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230321-linux-x86_64-iritkatriel-remove_JUMP_IF_FALSE-3.12.0a6+-12595f6 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.87 ms: 1.59x faster                                                       |
| python_startup_no_site | 5.78 ms                                                | 6.50 ms: 1.13x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.19x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230321-linux-x86_64-iritkatriel-remove_JUMP_IF_FALSE-3.12.0a6+-12595f6 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                | 10.0 ms: 1.46x faster                                                       |
| genshi_text     | 30.6 ms                                                | 21.8 ms: 1.41x faster                                                       |
| django_template | 46.3 ms                                                | 33.2 ms: 1.39x faster                                                       |
| genshi_xml      | 63.7 ms                                                | 46.8 ms: 1.36x faster                                                       |
| Geometric mean  | (ref)                                                  | 1.40x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230321-linux-x86_64-iritkatriel-remove_JUMP_IF_FALSE-3.12.0a6+-12595f6 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| generators              | 76.4 ms                                                | 29.2 ms: 2.62x faster                                                       |
| deltablue               | 7.28 ms                                                | 3.18 ms: 2.29x faster                                                       |
| scimark_sor             | 197 ms                                                 | 104 ms: 1.89x faster                                                        |
| logging_silent          | 176 ns                                                 | 98.4 ns: 1.79x faster                                                       |
| asyncio_tcp             | 914 ms                                                 | 512 ms: 1.79x faster                                                        |
| richards                | 75.2 ms                                                | 43.5 ms: 1.73x faster                                                       |
| spectral_norm           | 150 ms                                                 | 88.6 ms: 1.69x faster                                                       |
| go                      | 226 ms                                                 | 134 ms: 1.68x faster                                                        |
| pyflate                 | 676 ms                                                 | 407 ms: 1.66x faster                                                        |
| nbody                   | 144 ms                                                 | 87.2 ms: 1.65x faster                                                       |
| raytrace                | 467 ms                                                 | 283 ms: 1.65x faster                                                        |
| scimark_monte_carlo     | 109 ms                                                 | 66.2 ms: 1.64x faster                                                       |
| crypto_pyaes            | 117 ms                                                 | 73.4 ms: 1.59x faster                                                       |
| python_startup          | 14.1 ms                                                | 8.87 ms: 1.59x faster                                                       |
| chaos                   | 106 ms                                                 | 66.6 ms: 1.59x faster                                                       |
| pickle_pure_python      | 452 us                                                 | 287 us: 1.58x faster                                                        |
| hexiom                  | 9.43 ms                                                | 6.11 ms: 1.54x faster                                                       |
| unpickle_pure_python    | 302 us                                                 | 198 us: 1.52x faster                                                        |
| deepcopy_memo           | 51.7 us                                                | 34.6 us: 1.49x faster                                                       |
| float                   | 109 ms                                                 | 73.2 ms: 1.49x faster                                                       |
| scimark_lu              | 161 ms                                                 | 109 ms: 1.48x faster                                                        |
| mako                    | 14.7 ms                                                | 10.0 ms: 1.46x faster                                                       |
| coroutines              | 31.6 ms                                                | 22.0 ms: 1.44x faster                                                       |
| json_dumps              | 13.4 ms                                                | 9.51 ms: 1.41x faster                                                       |
| html5lib                | 85.9 ms                                                | 60.8 ms: 1.41x faster                                                       |
| sqlglot_parse           | 2.04 ms                                                | 1.45 ms: 1.41x faster                                                       |
| genshi_text             | 30.6 ms                                                | 21.8 ms: 1.41x faster                                                       |
| logging_simple          | 8.10 us                                                | 5.78 us: 1.40x faster                                                       |
| tornado_http            | 128 ms                                                 | 91.5 ms: 1.40x faster                                                       |
| logging_format          | 8.85 us                                                | 6.32 us: 1.40x faster                                                       |
| chameleon               | 9.17 ms                                                | 6.56 ms: 1.40x faster                                                       |
| sqlglot_transpile       | 2.43 ms                                                | 1.74 ms: 1.39x faster                                                       |
| django_template         | 46.3 ms                                                | 33.2 ms: 1.39x faster                                                       |
| async_tree_io           | 1.78 sec                                               | 1.30 sec: 1.37x faster                                                      |
| pprint_pformat          | 1.98 sec                                               | 1.45 sec: 1.37x faster                                                      |
| scimark_fft             | 421 ms                                                 | 309 ms: 1.36x faster                                                        |
| genshi_xml              | 63.7 ms                                                | 46.8 ms: 1.36x faster                                                       |
| pycparser               | 1.53 sec                                               | 1.13 sec: 1.36x faster                                                      |
| 2to3                    | 335 ms                                                 | 249 ms: 1.35x faster                                                        |
| async_tree_none         | 711 ms                                                 | 527 ms: 1.35x faster                                                        |
| unpack_sequence         | 59.4 ns                                                | 44.2 ns: 1.34x faster                                                       |
| pprint_safe_repr        | 953 ms                                                 | 711 ms: 1.34x faster                                                        |
| thrift                  | 1.03 ms                                                | 773 us: 1.34x faster                                                        |
| regex_compile           | 177 ms                                                 | 134 ms: 1.33x faster                                                        |
| aiohttp                 | 1.34 ms                                                | 1.01 ms: 1.33x faster                                                       |
| deepcopy                | 438 us                                                 | 330 us: 1.32x faster                                                        |
| fannkuch                | 488 ms                                                 | 371 ms: 1.32x faster                                                        |
| gunicorn                | 1.43 ms                                                | 1.09 ms: 1.31x faster                                                       |
| xml_etree_process       | 74.5 ms                                                | 56.8 ms: 1.31x faster                                                       |
| mypy2                   | 430 ms                                                 | 333 ms: 1.29x faster                                                        |
| async_tree_memoization  | 855 ms                                                 | 666 ms: 1.28x faster                                                        |
| async_tree_cpu_io_mixed | 949 ms                                                 | 746 ms: 1.27x faster                                                        |
| sqlglot_normalize       | 134 ms                                                 | 106 ms: 1.27x faster                                                        |
| deepcopy_reduce         | 3.79 us                                                | 2.98 us: 1.27x faster                                                       |
| sqlglot_optimize        | 65.2 ms                                                | 51.5 ms: 1.27x faster                                                       |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.32 ms: 1.26x faster                                                       |
| docutils                | 3.18 sec                                               | 2.54 sec: 1.25x faster                                                      |
| nqueens                 | 100 ms                                                 | 80.8 ms: 1.24x faster                                                       |
| sqlalchemy_declarative  | 165 ms                                                 | 136 ms: 1.21x faster                                                        |
| bench_thread_pool       | 946 us                                                 | 788 us: 1.20x faster                                                        |
| sqlalchemy_imperative   | 21.5 ms                                                | 17.9 ms: 1.20x faster                                                       |
| dulwich_log             | 75.8 ms                                                | 63.3 ms: 1.20x faster                                                       |
| json_loads              | 28.7 us                                                | 24.0 us: 1.19x faster                                                       |
| sympy_integrate         | 24.0 ms                                                | 20.4 ms: 1.18x faster                                                       |
| sympy_expand            | 534 ms                                                 | 459 ms: 1.16x faster                                                        |
| json                    | 5.35 ms                                                | 4.61 ms: 1.16x faster                                                       |
| pickle_list             | 4.72 us                                                | 4.08 us: 1.16x faster                                                       |
| xml_etree_generate      | 93.8 ms                                                | 81.6 ms: 1.15x faster                                                       |
| sympy_str               | 325 ms                                                 | 283 ms: 1.15x faster                                                        |
| regex_v8                | 25.0 ms                                                | 22.0 ms: 1.14x faster                                                       |
| djangocms               | 36.9 us                                                | 32.4 us: 1.14x faster                                                       |
| mdp                     | 2.74 sec                                               | 2.43 sec: 1.13x faster                                                      |
| pathlib                 | 20.0 ms                                                | 17.8 ms: 1.12x faster                                                       |
| sqlite_synth            | 2.92 us                                                | 2.61 us: 1.12x faster                                                       |
| sympy_sum               | 183 ms                                                 | 166 ms: 1.10x faster                                                        |
| meteor_contest          | 114 ms                                                 | 103 ms: 1.10x faster                                                        |
| create_gc_cycles        | 1.65 ms                                                | 1.50 ms: 1.10x faster                                                       |
| xml_etree_parse         | 163 ms                                                 | 150 ms: 1.09x faster                                                        |
| xml_etree_iterparse     | 111 ms                                                 | 103 ms: 1.08x faster                                                        |
| regex_dna               | 214 ms                                                 | 201 ms: 1.06x faster                                                        |
| async_generators        | 426 ms                                                 | 411 ms: 1.04x faster                                                        |
| telco                   | 6.73 ms                                                | 6.51 ms: 1.03x faster                                                       |
| pidigits                | 190 ms                                                 | 189 ms: 1.00x faster                                                        |
| unpickle_list           | 4.92 us                                                | 5.01 us: 1.02x slower                                                       |
| gc_traversal            | 3.53 ms                                                | 3.83 ms: 1.08x slower                                                       |
| pickle_dict             | 27.6 us                                                | 30.8 us: 1.12x slower                                                       |
| regex_effbot            | 3.19 ms                                                | 3.59 ms: 1.12x slower                                                       |
| python_startup_no_site  | 5.78 ms                                                | 6.50 ms: 1.13x slower                                                       |
| dask                    | 436 ms                                                 | 508 ms: 1.16x slower                                                        |
| coverage                | 74.7 ms                                                | 94.9 ms: 1.27x slower                                                       |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                                |

Benchmark hidden because not significant (3): unpickle, bench_mp_pool, pickle
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, pylint
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230321-3.12.0a6+-12595f6/bm-20230321-linux-x86_64-iritkatriel-remove_JUMP_IF_FALSE-3.12.0a6+-12595f6.json: comprehensions
