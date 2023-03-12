
# Results vs. 3.10.4

- fork: faster-cpython
- ref: experimental_no_cach
- machine: linux-x86_64
- commit hash: bbb99c1
- commit date: 2023-03-09
- overall geometric mean: 1.29x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230309-linux-x86_64-faster%2dcpython-experimental_no_cach-3.12.0a6+-bbb99c1 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 251 ms: 1.34x faster                                                             |
| chameleon      | 9.17 ms                                                | 6.54 ms: 1.40x faster                                                            |
| docutils       | 3.18 sec                                               | 2.55 sec: 1.25x faster                                                           |
| html5lib       | 85.9 ms                                                | 61.0 ms: 1.41x faster                                                            |
| tornado_http   | 128 ms                                                 | 95.1 ms: 1.35x faster                                                            |
| Geometric mean | (ref)                                                  | 1.35x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230309-linux-x86_64-faster%2dcpython-experimental_no_cach-3.12.0a6+-bbb99c1 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 144 ms                                                 | 95.1 ms: 1.51x faster                                                            |
| float          | 109 ms                                                 | 73.8 ms: 1.48x faster                                                            |
| pidigits       | 190 ms                                                 | 189 ms: 1.00x faster                                                             |
| Geometric mean | (ref)                                                  | 1.31x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230309-linux-x86_64-faster%2dcpython-experimental_no_cach-3.12.0a6+-bbb99c1 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 133 ms: 1.33x faster                                                             |
| regex_v8       | 25.0 ms                                                | 21.8 ms: 1.15x faster                                                            |
| regex_dna      | 214 ms                                                 | 205 ms: 1.04x faster                                                             |
| regex_effbot   | 3.19 ms                                                | 3.43 ms: 1.08x slower                                                            |
| Geometric mean | (ref)                                                  | 1.10x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230309-linux-x86_64-faster%2dcpython-experimental_no_cach-3.12.0a6+-bbb99c1 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 287 us: 1.57x faster                                                             |
| unpickle_pure_python | 302 us                                                 | 198 us: 1.53x faster                                                             |
| json_dumps           | 13.4 ms                                                | 9.51 ms: 1.41x faster                                                            |
| xml_etree_process    | 74.5 ms                                                | 55.7 ms: 1.34x faster                                                            |
| json_loads           | 28.7 us                                                | 24.1 us: 1.19x faster                                                            |
| pickle_list          | 4.72 us                                                | 4.04 us: 1.17x faster                                                            |
| xml_etree_generate   | 93.8 ms                                                | 80.7 ms: 1.16x faster                                                            |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.10x faster                                                             |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.08x faster                                                             |
| unpickle_list        | 4.92 us                                                | 4.98 us: 1.01x slower                                                            |
| pickle_dict          | 27.6 us                                                | 31.5 us: 1.14x slower                                                            |
| Geometric mean       | (ref)                                                  | 1.17x faster                                                                     |

Benchmark hidden because not significant (2): unpickle, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230309-linux-x86_64-faster%2dcpython-experimental_no_cach-3.12.0a6+-bbb99c1 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 9.02 ms: 1.56x faster                                                            |
| python_startup_no_site | 5.78 ms                                                | 6.54 ms: 1.13x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.17x faster                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230309-linux-x86_64-faster%2dcpython-experimental_no_cach-3.12.0a6+-bbb99c1 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                | 9.86 ms: 1.49x faster                                                            |
| genshi_text     | 30.6 ms                                                | 22.1 ms: 1.38x faster                                                            |
| django_template | 46.3 ms                                                | 33.8 ms: 1.37x faster                                                            |
| genshi_xml      | 63.7 ms                                                | 48.6 ms: 1.31x faster                                                            |
| Geometric mean  | (ref)                                                  | 1.39x faster                                                                     |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230309-linux-x86_64-faster%2dcpython-experimental_no_cach-3.12.0a6+-bbb99c1 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| generators              | 76.4 ms                                                | 29.8 ms: 2.57x faster                                                            |
| deltablue               | 7.28 ms                                                | 3.22 ms: 2.26x faster                                                            |
| scimark_sor             | 197 ms                                                 | 108 ms: 1.83x faster                                                             |
| asyncio_tcp             | 914 ms                                                 | 509 ms: 1.80x faster                                                             |
| logging_silent          | 176 ns                                                 | 98.4 ns: 1.79x faster                                                            |
| richards                | 75.2 ms                                                | 43.0 ms: 1.75x faster                                                            |
| go                      | 226 ms                                                 | 134 ms: 1.69x faster                                                             |
| pyflate                 | 676 ms                                                 | 410 ms: 1.65x faster                                                             |
| raytrace                | 467 ms                                                 | 283 ms: 1.65x faster                                                             |
| scimark_monte_carlo     | 109 ms                                                 | 67.1 ms: 1.62x faster                                                            |
| pickle_pure_python      | 452 us                                                 | 287 us: 1.57x faster                                                             |
| crypto_pyaes            | 117 ms                                                 | 74.3 ms: 1.57x faster                                                            |
| chaos                   | 106 ms                                                 | 67.5 ms: 1.56x faster                                                            |
| python_startup          | 14.1 ms                                                | 9.02 ms: 1.56x faster                                                            |
| spectral_norm           | 150 ms                                                 | 96.9 ms: 1.54x faster                                                            |
| hexiom                  | 9.43 ms                                                | 6.16 ms: 1.53x faster                                                            |
| unpickle_pure_python    | 302 us                                                 | 198 us: 1.53x faster                                                             |
| deepcopy_memo           | 51.7 us                                                | 34.0 us: 1.52x faster                                                            |
| nbody                   | 144 ms                                                 | 95.1 ms: 1.51x faster                                                            |
| mako                    | 14.7 ms                                                | 9.86 ms: 1.49x faster                                                            |
| float                   | 109 ms                                                 | 73.8 ms: 1.48x faster                                                            |
| scimark_lu              | 161 ms                                                 | 111 ms: 1.45x faster                                                             |
| sqlglot_parse           | 2.04 ms                                                | 1.43 ms: 1.43x faster                                                            |
| pprint_pformat          | 1.98 sec                                               | 1.39 sec: 1.42x faster                                                           |
| sqlglot_transpile       | 2.43 ms                                                | 1.72 ms: 1.42x faster                                                            |
| json_dumps              | 13.4 ms                                                | 9.51 ms: 1.41x faster                                                            |
| logging_format          | 8.85 us                                                | 6.27 us: 1.41x faster                                                            |
| html5lib                | 85.9 ms                                                | 61.0 ms: 1.41x faster                                                            |
| chameleon               | 9.17 ms                                                | 6.54 ms: 1.40x faster                                                            |
| pprint_safe_repr        | 953 ms                                                 | 680 ms: 1.40x faster                                                             |
| logging_simple          | 8.10 us                                                | 5.81 us: 1.39x faster                                                            |
| coroutines              | 31.6 ms                                                | 22.8 ms: 1.39x faster                                                            |
| unpack_sequence         | 59.4 ns                                                | 42.8 ns: 1.39x faster                                                            |
| genshi_text             | 30.6 ms                                                | 22.1 ms: 1.38x faster                                                            |
| async_tree_io           | 1.78 sec                                               | 1.29 sec: 1.38x faster                                                           |
| django_template         | 46.3 ms                                                | 33.8 ms: 1.37x faster                                                            |
| async_tree_none         | 711 ms                                                 | 526 ms: 1.35x faster                                                             |
| tornado_http            | 128 ms                                                 | 95.1 ms: 1.35x faster                                                            |
| xml_etree_process       | 74.5 ms                                                | 55.7 ms: 1.34x faster                                                            |
| 2to3                    | 335 ms                                                 | 251 ms: 1.34x faster                                                             |
| regex_compile           | 177 ms                                                 | 133 ms: 1.33x faster                                                             |
| fannkuch                | 488 ms                                                 | 366 ms: 1.33x faster                                                             |
| pycparser               | 1.53 sec                                               | 1.15 sec: 1.33x faster                                                           |
| aiohttp                 | 1.34 ms                                                | 1.01 ms: 1.33x faster                                                            |
| scimark_fft             | 421 ms                                                 | 317 ms: 1.33x faster                                                             |
| thrift                  | 1.03 ms                                                | 780 us: 1.33x faster                                                             |
| deepcopy                | 438 us                                                 | 333 us: 1.31x faster                                                             |
| gunicorn                | 1.43 ms                                                | 1.09 ms: 1.31x faster                                                            |
| genshi_xml              | 63.7 ms                                                | 48.6 ms: 1.31x faster                                                            |
| async_tree_memoization  | 855 ms                                                 | 657 ms: 1.30x faster                                                             |
| sqlglot_normalize       | 134 ms                                                 | 103 ms: 1.30x faster                                                             |
| mypy2                   | 430 ms                                                 | 333 ms: 1.29x faster                                                             |
| sqlglot_optimize        | 65.2 ms                                                | 50.6 ms: 1.29x faster                                                            |
| async_tree_cpu_io_mixed | 949 ms                                                 | 744 ms: 1.28x faster                                                             |
| deepcopy_reduce         | 3.79 us                                                | 2.99 us: 1.27x faster                                                            |
| docutils                | 3.18 sec                                               | 2.55 sec: 1.25x faster                                                           |
| nqueens                 | 100 ms                                                 | 81.0 ms: 1.24x faster                                                            |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.50 ms: 1.21x faster                                                            |
| sqlalchemy_declarative  | 165 ms                                                 | 137 ms: 1.20x faster                                                             |
| bench_thread_pool       | 946 us                                                 | 789 us: 1.20x faster                                                             |
| dulwich_log             | 75.8 ms                                                | 63.9 ms: 1.19x faster                                                            |
| json_loads              | 28.7 us                                                | 24.1 us: 1.19x faster                                                            |
| sqlalchemy_imperative   | 21.5 ms                                                | 18.1 ms: 1.18x faster                                                            |
| sympy_integrate         | 24.0 ms                                                | 20.5 ms: 1.18x faster                                                            |
| pickle_list             | 4.72 us                                                | 4.04 us: 1.17x faster                                                            |
| xml_etree_generate      | 93.8 ms                                                | 80.7 ms: 1.16x faster                                                            |
| json                    | 5.35 ms                                                | 4.60 ms: 1.16x faster                                                            |
| sympy_expand            | 534 ms                                                 | 462 ms: 1.16x faster                                                             |
| regex_v8                | 25.0 ms                                                | 21.8 ms: 1.15x faster                                                            |
| sympy_str               | 325 ms                                                 | 284 ms: 1.14x faster                                                             |
| mdp                     | 2.74 sec                                               | 2.42 sec: 1.14x faster                                                           |
| djangocms               | 36.9 us                                                | 32.7 us: 1.13x faster                                                            |
| pathlib                 | 20.0 ms                                                | 17.7 ms: 1.13x faster                                                            |
| sqlite_synth            | 2.92 us                                                | 2.61 us: 1.12x faster                                                            |
| create_gc_cycles        | 1.65 ms                                                | 1.49 ms: 1.11x faster                                                            |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.10x faster                                                             |
| meteor_contest          | 114 ms                                                 | 104 ms: 1.10x faster                                                             |
| sympy_sum               | 183 ms                                                 | 167 ms: 1.10x faster                                                             |
| xml_etree_iterparse     | 111 ms                                                 | 103 ms: 1.08x faster                                                             |
| regex_dna               | 214 ms                                                 | 205 ms: 1.04x faster                                                             |
| async_generators        | 426 ms                                                 | 411 ms: 1.04x faster                                                             |
| telco                   | 6.73 ms                                                | 6.59 ms: 1.02x faster                                                            |
| pidigits                | 190 ms                                                 | 189 ms: 1.00x faster                                                             |
| unpickle_list           | 4.92 us                                                | 4.98 us: 1.01x slower                                                            |
| gc_traversal            | 3.53 ms                                                | 3.77 ms: 1.07x slower                                                            |
| regex_effbot            | 3.19 ms                                                | 3.43 ms: 1.08x slower                                                            |
| python_startup_no_site  | 5.78 ms                                                | 6.54 ms: 1.13x slower                                                            |
| pickle_dict             | 27.6 us                                                | 31.5 us: 1.14x slower                                                            |
| dask                    | 436 ms                                                 | 509 ms: 1.17x slower                                                             |
| coverage                | 74.7 ms                                                | 96.0 ms: 1.28x slower                                                            |
| Geometric mean          | (ref)                                                  | 1.29x faster                                                                     |

Benchmark hidden because not significant (3): unpickle, bench_mp_pool, pickle
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, pylint
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230309-3.12.0a6+-bbb99c1/bm-20230309-linux-x86_64-faster%2dcpython-experimental_no_cach-3.12.0a6+-bbb99c1.json: comprehensions
