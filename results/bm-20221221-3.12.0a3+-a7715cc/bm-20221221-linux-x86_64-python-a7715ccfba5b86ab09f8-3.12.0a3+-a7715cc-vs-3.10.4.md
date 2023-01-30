
# Results vs. 3.10.4

- fork: python
- ref: a7715ccfba5b86ab09f8
- machine: linux-x86_64
- commit hash: a7715cc
- commit date: 2022-12-21
- overall geometric mean: 1.31x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221221-linux-x86_64-python-a7715ccfba5b86ab09f8-3.12.0a3+-a7715cc |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 332 ms                                                 | 253 ms: 1.31x faster                                                   |
| chameleon      | 8.86 ms                                                | 6.36 ms: 1.39x faster                                                  |
| docutils       | 3.18 sec                                               | 2.48 sec: 1.28x faster                                                 |
| html5lib       | 85.8 ms                                                | 59.5 ms: 1.44x faster                                                  |
| Geometric mean | (ref)                                                  | 1.36x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221221-linux-x86_64-python-a7715ccfba5b86ab09f8-3.12.0a3+-a7715cc |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 108 ms                                                 | 71.8 ms: 1.50x faster                                                  |
| nbody          | 136 ms                                                 | 93.1 ms: 1.46x faster                                                  |
| pidigits       | 190 ms                                                 | 197 ms: 1.04x slower                                                   |
| Geometric mean | (ref)                                                  | 1.28x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221221-linux-x86_64-python-a7715ccfba5b86ab09f8-3.12.0a3+-a7715cc |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 174 ms                                                 | 130 ms: 1.33x faster                                                   |
| regex_v8       | 25.0 ms                                                | 21.7 ms: 1.15x faster                                                  |
| regex_dna      | 214 ms                                                 | 203 ms: 1.05x faster                                                   |
| regex_effbot   | 3.21 ms                                                | 3.45 ms: 1.08x slower                                                  |
| Geometric mean | (ref)                                                  | 1.11x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221221-linux-x86_64-python-a7715ccfba5b86ab09f8-3.12.0a3+-a7715cc |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 453 us                                                 | 283 us: 1.60x faster                                                   |
| unpickle_pure_python | 297 us                                                 | 197 us: 1.51x faster                                                   |
| json_dumps           | 13.5 ms                                                | 9.43 ms: 1.43x faster                                                  |
| xml_etree_process    | 74.5 ms                                                | 53.5 ms: 1.39x faster                                                  |
| json_loads           | 28.9 us                                                | 23.6 us: 1.22x faster                                                  |
| xml_etree_generate   | 93.3 ms                                                | 76.5 ms: 1.22x faster                                                  |
| pickle_list          | 4.50 us                                                | 3.98 us: 1.13x faster                                                  |
| xml_etree_parse      | 163 ms                                                 | 147 ms: 1.11x faster                                                   |
| unpickle             | 14.3 us                                                | 13.2 us: 1.08x faster                                                  |
| xml_etree_iterparse  | 110 ms                                                 | 106 ms: 1.04x faster                                                   |
| unpickle_list        | 4.99 us                                                | 4.93 us: 1.01x faster                                                  |
| pickle               | 10.1 us                                                | 10.4 us: 1.03x slower                                                  |
| pickle_dict          | 28.3 us                                                | 30.6 us: 1.08x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.19x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221221-linux-x86_64-python-a7715ccfba5b86ab09f8-3.12.0a3+-a7715cc |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 13.9 ms                                                | 8.43 ms: 1.65x faster                                                  |
| python_startup_no_site | 5.76 ms                                                | 6.09 ms: 1.06x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.25x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221221-linux-x86_64-python-a7715ccfba5b86ab09f8-3.12.0a3+-a7715cc |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 14.3 ms                                                | 9.47 ms: 1.51x faster                                                  |
| genshi_text     | 30.6 ms                                                | 20.4 ms: 1.50x faster                                                  |
| django_template | 46.3 ms                                                | 32.5 ms: 1.43x faster                                                  |
| genshi_xml      | 63.6 ms                                                | 47.6 ms: 1.33x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.44x faster                                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221221-linux-x86_64-python-a7715ccfba5b86ab09f8-3.12.0a3+-a7715cc |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| deltablue               | 7.39 ms                                                | 3.20 ms: 2.31x faster                                                  |
| logging_silent          | 173 ns                                                 | 90.4 ns: 1.92x faster                                                  |
| scimark_sor             | 193 ms                                                 | 105 ms: 1.83x faster                                                   |
| richards                | 71.4 ms                                                | 41.4 ms: 1.73x faster                                                  |
| pyflate                 | 675 ms                                                 | 396 ms: 1.70x faster                                                   |
| python_startup          | 13.9 ms                                                | 8.43 ms: 1.65x faster                                                  |
| raytrace                | 461 ms                                                 | 280 ms: 1.65x faster                                                   |
| go                      | 226 ms                                                 | 138 ms: 1.64x faster                                                   |
| scimark_monte_carlo     | 105 ms                                                 | 64.2 ms: 1.63x faster                                                  |
| pickle_pure_python      | 453 us                                                 | 283 us: 1.60x faster                                                   |
| crypto_pyaes            | 118 ms                                                 | 74.4 ms: 1.58x faster                                                  |
| hexiom                  | 9.42 ms                                                | 6.02 ms: 1.56x faster                                                  |
| spectral_norm           | 148 ms                                                 | 94.8 ms: 1.56x faster                                                  |
| chaos                   | 104 ms                                                 | 68.7 ms: 1.52x faster                                                  |
| unpickle_pure_python    | 297 us                                                 | 197 us: 1.51x faster                                                   |
| mako                    | 14.3 ms                                                | 9.47 ms: 1.51x faster                                                  |
| float                   | 108 ms                                                 | 71.8 ms: 1.50x faster                                                  |
| genshi_text             | 30.6 ms                                                | 20.4 ms: 1.50x faster                                                  |
| scimark_lu              | 158 ms                                                 | 107 ms: 1.49x faster                                                   |
| deepcopy_memo           | 50.0 us                                                | 33.9 us: 1.47x faster                                                  |
| sqlglot_parse           | 2.04 ms                                                | 1.39 ms: 1.46x faster                                                  |
| nbody                   | 136 ms                                                 | 93.1 ms: 1.46x faster                                                  |
| pprint_pformat          | 1.97 sec                                               | 1.36 sec: 1.45x faster                                                 |
| html5lib                | 85.8 ms                                                | 59.5 ms: 1.44x faster                                                  |
| sqlglot_transpile       | 2.42 ms                                                | 1.68 ms: 1.44x faster                                                  |
| unpack_sequence         | 59.5 ns                                                | 41.3 ns: 1.44x faster                                                  |
| logging_format          | 8.92 us                                                | 6.22 us: 1.43x faster                                                  |
| json_dumps              | 13.5 ms                                                | 9.43 ms: 1.43x faster                                                  |
| pprint_safe_repr        | 943 ms                                                 | 661 ms: 1.43x faster                                                   |
| django_template         | 46.3 ms                                                | 32.5 ms: 1.43x faster                                                  |
| logging_simple          | 8.06 us                                                | 5.68 us: 1.42x faster                                                  |
| chameleon               | 8.86 ms                                                | 6.36 ms: 1.39x faster                                                  |
| thrift                  | 1.03 ms                                                | 741 us: 1.39x faster                                                   |
| xml_etree_process       | 74.5 ms                                                | 53.5 ms: 1.39x faster                                                  |
| pycparser               | 1.51 sec                                               | 1.10 sec: 1.38x faster                                                 |
| async_tree_io           | 1.78 sec                                               | 1.32 sec: 1.35x faster                                                 |
| scimark_fft             | 414 ms                                                 | 309 ms: 1.34x faster                                                   |
| scimark_sparse_mat_mult | 5.48 ms                                                | 4.10 ms: 1.34x faster                                                  |
| regex_compile           | 174 ms                                                 | 130 ms: 1.33x faster                                                   |
| genshi_xml              | 63.6 ms                                                | 47.6 ms: 1.33x faster                                                  |
| async_tree_none         | 713 ms                                                 | 535 ms: 1.33x faster                                                   |
| async_tree_memoization  | 854 ms                                                 | 644 ms: 1.33x faster                                                   |
| 2to3                    | 332 ms                                                 | 253 ms: 1.31x faster                                                   |
| fannkuch                | 477 ms                                                 | 363 ms: 1.31x faster                                                   |
| deepcopy                | 429 us                                                 | 328 us: 1.31x faster                                                   |
| sqlglot_optimize        | 65.3 ms                                                | 50.1 ms: 1.30x faster                                                  |
| sqlglot_normalize       | 135 ms                                                 | 104 ms: 1.30x faster                                                   |
| deepcopy_reduce         | 3.75 us                                                | 2.90 us: 1.29x faster                                                  |
| coroutines              | 31.7 ms                                                | 24.5 ms: 1.29x faster                                                  |
| docutils                | 3.18 sec                                               | 2.48 sec: 1.28x faster                                                 |
| nqueens                 | 99.3 ms                                                | 78.5 ms: 1.27x faster                                                  |
| mypy                    | 1.01 sec                                               | 803 ms: 1.26x faster                                                   |
| async_tree_cpu_io_mixed | 949 ms                                                 | 765 ms: 1.24x faster                                                   |
| json_loads              | 28.9 us                                                | 23.6 us: 1.22x faster                                                  |
| xml_etree_generate      | 93.3 ms                                                | 76.5 ms: 1.22x faster                                                  |
| dulwich_log             | 75.5 ms                                                | 62.6 ms: 1.21x faster                                                  |
| bench_thread_pool       | 943 us                                                 | 783 us: 1.20x faster                                                   |
| async_generators        | 428 ms                                                 | 356 ms: 1.20x faster                                                   |
| sympy_expand            | 537 ms                                                 | 451 ms: 1.19x faster                                                   |
| sympy_integrate         | 23.9 ms                                                | 20.2 ms: 1.18x faster                                                  |
| sympy_str               | 324 ms                                                 | 280 ms: 1.16x faster                                                   |
| json                    | 5.35 ms                                                | 4.63 ms: 1.16x faster                                                  |
| regex_v8                | 25.0 ms                                                | 21.7 ms: 1.15x faster                                                  |
| pickle_list             | 4.50 us                                                | 3.98 us: 1.13x faster                                                  |
| sympy_sum               | 183 ms                                                 | 162 ms: 1.13x faster                                                   |
| sqlite_synth            | 2.90 us                                                | 2.58 us: 1.13x faster                                                  |
| pathlib                 | 20.0 ms                                                | 17.9 ms: 1.12x faster                                                  |
| xml_etree_parse         | 163 ms                                                 | 147 ms: 1.11x faster                                                   |
| mdp                     | 2.82 sec                                               | 2.54 sec: 1.11x faster                                                 |
| meteor_contest          | 114 ms                                                 | 104 ms: 1.10x faster                                                   |
| unpickle                | 14.3 us                                                | 13.2 us: 1.08x faster                                                  |
| telco                   | 6.68 ms                                                | 6.29 ms: 1.06x faster                                                  |
| regex_dna               | 214 ms                                                 | 203 ms: 1.05x faster                                                   |
| xml_etree_iterparse     | 110 ms                                                 | 106 ms: 1.04x faster                                                   |
| unpickle_list           | 4.99 us                                                | 4.93 us: 1.01x faster                                                  |
| generators              | 75.8 ms                                                | 77.4 ms: 1.02x slower                                                  |
| pickle                  | 10.1 us                                                | 10.4 us: 1.03x slower                                                  |
| pidigits                | 190 ms                                                 | 197 ms: 1.04x slower                                                   |
| python_startup_no_site  | 5.76 ms                                                | 6.09 ms: 1.06x slower                                                  |
| regex_effbot            | 3.21 ms                                                | 3.45 ms: 1.08x slower                                                  |
| pickle_dict             | 28.3 us                                                | 30.6 us: 1.08x slower                                                  |
| coverage                | 75.3 ms                                                | 102 ms: 1.35x slower                                                   |
| Geometric mean          | (ref)                                                  | 1.31x faster                                                           |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (7) of /home/mdboom/Work/builds/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
