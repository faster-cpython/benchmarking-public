
# Results vs. 3.10.4

- fork: python
- ref: a7715ccfba5b86ab09f8
- machine: linux-x86_64
- commit hash: a7715cc
- commit date: 2022-12-21
- overall geometric mean: 1.31x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221221-linux-x86_64-python-a7715ccfba5b86ab09f8-3.12.0a3+-a7715cc |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 253 ms: 1.33x faster                                                   |
| chameleon      | 9.17 ms                                                | 6.36 ms: 1.44x faster                                                  |
| docutils       | 3.18 sec                                               | 2.48 sec: 1.28x faster                                                 |
| html5lib       | 85.9 ms                                                | 59.5 ms: 1.44x faster                                                  |
| Geometric mean | (ref)                                                  | 1.37x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221221-linux-x86_64-python-a7715ccfba5b86ab09f8-3.12.0a3+-a7715cc |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 144 ms                                                 | 93.1 ms: 1.55x faster                                                  |
| float          | 109 ms                                                 | 71.8 ms: 1.52x faster                                                  |
| pidigits       | 190 ms                                                 | 197 ms: 1.04x slower                                                   |
| Geometric mean | (ref)                                                  | 1.31x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221221-linux-x86_64-python-a7715ccfba5b86ab09f8-3.12.0a3+-a7715cc |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 130 ms: 1.36x faster                                                   |
| regex_v8       | 25.0 ms                                                | 21.7 ms: 1.16x faster                                                  |
| regex_dna      | 214 ms                                                 | 203 ms: 1.05x faster                                                   |
| regex_effbot   | 3.19 ms                                                | 3.45 ms: 1.08x slower                                                  |
| Geometric mean | (ref)                                                  | 1.11x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221221-linux-x86_64-python-a7715ccfba5b86ab09f8-3.12.0a3+-a7715cc |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 283 us: 1.60x faster                                                   |
| unpickle_pure_python | 302 us                                                 | 197 us: 1.53x faster                                                   |
| json_dumps           | 13.4 ms                                                | 9.43 ms: 1.43x faster                                                  |
| xml_etree_process    | 74.5 ms                                                | 53.5 ms: 1.39x faster                                                  |
| xml_etree_generate   | 93.8 ms                                                | 76.5 ms: 1.23x faster                                                  |
| json_loads           | 28.7 us                                                | 23.6 us: 1.21x faster                                                  |
| pickle_list          | 4.72 us                                                | 3.98 us: 1.19x faster                                                  |
| xml_etree_parse      | 163 ms                                                 | 147 ms: 1.11x faster                                                   |
| unpickle             | 14.2 us                                                | 13.2 us: 1.07x faster                                                  |
| xml_etree_iterparse  | 111 ms                                                 | 106 ms: 1.05x faster                                                   |
| pickle               | 10.2 us                                                | 10.4 us: 1.02x slower                                                  |
| pickle_dict          | 27.6 us                                                | 30.6 us: 1.11x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.19x faster                                                           |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221221-linux-x86_64-python-a7715ccfba5b86ab09f8-3.12.0a3+-a7715cc |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.43 ms: 1.67x faster                                                  |
| python_startup_no_site | 5.78 ms                                                | 6.09 ms: 1.05x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.26x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221221-linux-x86_64-python-a7715ccfba5b86ab09f8-3.12.0a3+-a7715cc |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 14.7 ms                                                | 9.47 ms: 1.55x faster                                                  |
| genshi_text     | 30.6 ms                                                | 20.4 ms: 1.50x faster                                                  |
| django_template | 46.3 ms                                                | 32.5 ms: 1.43x faster                                                  |
| genshi_xml      | 63.7 ms                                                | 47.6 ms: 1.34x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.45x faster                                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221221-linux-x86_64-python-a7715ccfba5b86ab09f8-3.12.0a3+-a7715cc |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| deltablue               | 7.28 ms                                                | 3.20 ms: 2.27x faster                                                  |
| logging_silent          | 176 ns                                                 | 90.4 ns: 1.95x faster                                                  |
| scimark_sor             | 197 ms                                                 | 105 ms: 1.87x faster                                                   |
| richards                | 75.2 ms                                                | 41.4 ms: 1.82x faster                                                  |
| pyflate                 | 676 ms                                                 | 396 ms: 1.70x faster                                                   |
| scimark_monte_carlo     | 109 ms                                                 | 64.2 ms: 1.69x faster                                                  |
| python_startup          | 14.1 ms                                                | 8.43 ms: 1.67x faster                                                  |
| raytrace                | 467 ms                                                 | 280 ms: 1.67x faster                                                   |
| go                      | 226 ms                                                 | 138 ms: 1.64x faster                                                   |
| pickle_pure_python      | 452 us                                                 | 283 us: 1.60x faster                                                   |
| spectral_norm           | 150 ms                                                 | 94.8 ms: 1.58x faster                                                  |
| crypto_pyaes            | 117 ms                                                 | 74.4 ms: 1.57x faster                                                  |
| hexiom                  | 9.43 ms                                                | 6.02 ms: 1.57x faster                                                  |
| mako                    | 14.7 ms                                                | 9.47 ms: 1.55x faster                                                  |
| nbody                   | 144 ms                                                 | 93.1 ms: 1.55x faster                                                  |
| chaos                   | 106 ms                                                 | 68.7 ms: 1.54x faster                                                  |
| unpickle_pure_python    | 302 us                                                 | 197 us: 1.53x faster                                                   |
| deepcopy_memo           | 51.7 us                                                | 33.9 us: 1.52x faster                                                  |
| float                   | 109 ms                                                 | 71.8 ms: 1.52x faster                                                  |
| scimark_lu              | 161 ms                                                 | 107 ms: 1.51x faster                                                   |
| genshi_text             | 30.6 ms                                                | 20.4 ms: 1.50x faster                                                  |
| sqlglot_parse           | 2.04 ms                                                | 1.39 ms: 1.47x faster                                                  |
| pprint_pformat          | 1.98 sec                                               | 1.36 sec: 1.46x faster                                                 |
| sqlglot_transpile       | 2.43 ms                                                | 1.68 ms: 1.45x faster                                                  |
| html5lib                | 85.9 ms                                                | 59.5 ms: 1.44x faster                                                  |
| chameleon               | 9.17 ms                                                | 6.36 ms: 1.44x faster                                                  |
| pprint_safe_repr        | 953 ms                                                 | 661 ms: 1.44x faster                                                   |
| unpack_sequence         | 59.4 ns                                                | 41.3 ns: 1.44x faster                                                  |
| django_template         | 46.3 ms                                                | 32.5 ms: 1.43x faster                                                  |
| logging_simple          | 8.10 us                                                | 5.68 us: 1.43x faster                                                  |
| json_dumps              | 13.4 ms                                                | 9.43 ms: 1.43x faster                                                  |
| logging_format          | 8.85 us                                                | 6.22 us: 1.42x faster                                                  |
| thrift                  | 1.03 ms                                                | 741 us: 1.40x faster                                                   |
| pycparser               | 1.53 sec                                               | 1.10 sec: 1.39x faster                                                 |
| xml_etree_process       | 74.5 ms                                                | 53.5 ms: 1.39x faster                                                  |
| scimark_fft             | 421 ms                                                 | 309 ms: 1.36x faster                                                   |
| regex_compile           | 177 ms                                                 | 130 ms: 1.36x faster                                                   |
| async_tree_io           | 1.78 sec                                               | 1.32 sec: 1.35x faster                                                 |
| fannkuch                | 488 ms                                                 | 363 ms: 1.34x faster                                                   |
| genshi_xml              | 63.7 ms                                                | 47.6 ms: 1.34x faster                                                  |
| deepcopy                | 438 us                                                 | 328 us: 1.34x faster                                                   |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.10 ms: 1.33x faster                                                  |
| async_tree_none         | 711 ms                                                 | 535 ms: 1.33x faster                                                   |
| async_tree_memoization  | 855 ms                                                 | 644 ms: 1.33x faster                                                   |
| 2to3                    | 335 ms                                                 | 253 ms: 1.33x faster                                                   |
| deepcopy_reduce         | 3.79 us                                                | 2.90 us: 1.31x faster                                                  |
| sqlglot_optimize        | 65.2 ms                                                | 50.1 ms: 1.30x faster                                                  |
| sqlglot_normalize       | 134 ms                                                 | 104 ms: 1.30x faster                                                   |
| coroutines              | 31.6 ms                                                | 24.5 ms: 1.29x faster                                                  |
| docutils                | 3.18 sec                                               | 2.48 sec: 1.28x faster                                                 |
| nqueens                 | 100 ms                                                 | 78.5 ms: 1.28x faster                                                  |
| async_tree_cpu_io_mixed | 949 ms                                                 | 765 ms: 1.24x faster                                                   |
| xml_etree_generate      | 93.8 ms                                                | 76.5 ms: 1.23x faster                                                  |
| json_loads              | 28.7 us                                                | 23.6 us: 1.21x faster                                                  |
| dulwich_log             | 75.8 ms                                                | 62.6 ms: 1.21x faster                                                  |
| bench_thread_pool       | 946 us                                                 | 783 us: 1.21x faster                                                   |
| async_generators        | 426 ms                                                 | 356 ms: 1.20x faster                                                   |
| sympy_integrate         | 24.0 ms                                                | 20.2 ms: 1.19x faster                                                  |
| pickle_list             | 4.72 us                                                | 3.98 us: 1.19x faster                                                  |
| sympy_expand            | 534 ms                                                 | 451 ms: 1.18x faster                                                   |
| sympy_str               | 325 ms                                                 | 280 ms: 1.16x faster                                                   |
| regex_v8                | 25.0 ms                                                | 21.7 ms: 1.16x faster                                                  |
| json                    | 5.35 ms                                                | 4.63 ms: 1.15x faster                                                  |
| sqlite_synth            | 2.92 us                                                | 2.58 us: 1.14x faster                                                  |
| sympy_sum               | 183 ms                                                 | 162 ms: 1.13x faster                                                   |
| pathlib                 | 20.0 ms                                                | 17.9 ms: 1.12x faster                                                  |
| xml_etree_parse         | 163 ms                                                 | 147 ms: 1.11x faster                                                   |
| meteor_contest          | 114 ms                                                 | 104 ms: 1.10x faster                                                   |
| mdp                     | 2.74 sec                                               | 2.54 sec: 1.08x faster                                                 |
| unpickle                | 14.2 us                                                | 13.2 us: 1.07x faster                                                  |
| telco                   | 6.73 ms                                                | 6.29 ms: 1.07x faster                                                  |
| regex_dna               | 214 ms                                                 | 203 ms: 1.05x faster                                                   |
| xml_etree_iterparse     | 111 ms                                                 | 106 ms: 1.05x faster                                                   |
| generators              | 76.4 ms                                                | 77.4 ms: 1.01x slower                                                  |
| pickle                  | 10.2 us                                                | 10.4 us: 1.02x slower                                                  |
| pidigits                | 190 ms                                                 | 197 ms: 1.04x slower                                                   |
| python_startup_no_site  | 5.78 ms                                                | 6.09 ms: 1.05x slower                                                  |
| regex_effbot            | 3.19 ms                                                | 3.45 ms: 1.08x slower                                                  |
| pickle_dict             | 27.6 us                                                | 30.6 us: 1.11x slower                                                  |
| coverage                | 74.7 ms                                                | 102 ms: 1.36x slower                                                   |
| Geometric mean          | (ref)                                                  | 1.31x faster                                                           |

Benchmark hidden because not significant (2): bench_mp_pool, unpickle_list
Ignored benchmarks (13) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, create_gc_cycles, dask, djangocms, flaskblogging, gc_traversal, gunicorn, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20221221-3.12.0a3+-a7715cc/bm-20221221-linux-x86_64-python-a7715ccfba5b86ab09f8-3.12.0a3+-a7715cc.json: mypy
