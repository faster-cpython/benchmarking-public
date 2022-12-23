Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-79daf93 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 332 ms                                                 | 253 ms: 1.31x faster                                                     |
| chameleon      | 8.86 ms                                                | 6.54 ms: 1.35x faster                                                    |
| docutils       | 3.18 sec                                               | 2.55 sec: 1.25x faster                                                   |
| html5lib       | 85.8 ms                                                | 59.8 ms: 1.43x faster                                                    |
| Geometric mean | (ref)                                                  | 1.34x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-79daf93 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 108 ms                                                 | 73.2 ms: 1.47x faster                                                    |
| nbody          | 136 ms                                                 | 94.7 ms: 1.44x faster                                                    |
| pidigits       | 190 ms                                                 | 193 ms: 1.01x slower                                                     |
| Geometric mean | (ref)                                                  | 1.28x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-79daf93 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 174 ms                                                 | 131 ms: 1.33x faster                                                     |
| regex_dna      | 214 ms                                                 | 204 ms: 1.05x faster                                                     |
| regex_effbot   | 3.21 ms                                                | 3.43 ms: 1.07x slower                                                    |
| regex_v8       | 25.0 ms                                                | 21.9 ms: 1.14x faster                                                    |
| Geometric mean | (ref)                                                  | 1.10x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-79daf93 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| json_dumps           | 13.5 ms                                                | 9.32 ms: 1.45x faster                                                    |
| json_loads           | 28.9 us                                                | 24.1 us: 1.20x faster                                                    |
| pickle_dict          | 28.3 us                                                | 31.2 us: 1.10x slower                                                    |
| pickle_list          | 4.50 us                                                | 4.11 us: 1.10x faster                                                    |
| pickle_pure_python   | 453 us                                                 | 278 us: 1.63x faster                                                     |
| unpickle             | 14.3 us                                                | 13.2 us: 1.08x faster                                                    |
| unpickle_pure_python | 297 us                                                 | 198 us: 1.50x faster                                                     |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.10x faster                                                     |
| xml_etree_iterparse  | 110 ms                                                 | 107 ms: 1.03x faster                                                     |
| xml_etree_generate   | 93.3 ms                                                | 78.1 ms: 1.19x faster                                                    |
| xml_etree_process    | 74.5 ms                                                | 54.0 ms: 1.38x faster                                                    |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                             |

Benchmark hidden because not significant (2): pickle, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-79daf93 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 13.9 ms                                                | 8.56 ms: 1.63x faster                                                    |
| python_startup_no_site | 5.76 ms                                                | 6.12 ms: 1.06x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.24x faster                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-79daf93 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 46.3 ms                                                | 32.5 ms: 1.42x faster                                                    |
| genshi_text     | 30.6 ms                                                | 20.5 ms: 1.49x faster                                                    |
| genshi_xml      | 63.6 ms                                                | 47.4 ms: 1.34x faster                                                    |
| mako            | 14.3 ms                                                | 9.51 ms: 1.50x faster                                                    |
| Geometric mean  | (ref)                                                  | 1.44x faster                                                             |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-79daf93 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3                    | 332 ms                                                 | 253 ms: 1.31x faster                                                     |
| async_generators        | 428 ms                                                 | 349 ms: 1.23x faster                                                     |
| async_tree_none         | 713 ms                                                 | 537 ms: 1.33x faster                                                     |
| async_tree_cpu_io_mixed | 949 ms                                                 | 768 ms: 1.24x faster                                                     |
| async_tree_io           | 1.78 sec                                               | 1.34 sec: 1.33x faster                                                   |
| async_tree_memoization  | 854 ms                                                 | 651 ms: 1.31x faster                                                     |
| chameleon               | 8.86 ms                                                | 6.54 ms: 1.35x faster                                                    |
| chaos                   | 104 ms                                                 | 66.4 ms: 1.57x faster                                                    |
| bench_thread_pool       | 943 us                                                 | 778 us: 1.21x faster                                                     |
| coroutines              | 31.7 ms                                                | 24.8 ms: 1.28x faster                                                    |
| coverage                | 75.3 ms                                                | 97.5 ms: 1.29x slower                                                    |
| crypto_pyaes            | 118 ms                                                 | 75.9 ms: 1.55x faster                                                    |
| deepcopy                | 429 us                                                 | 322 us: 1.33x faster                                                     |
| deepcopy_reduce         | 3.75 us                                                | 2.89 us: 1.30x faster                                                    |
| deepcopy_memo           | 50.0 us                                                | 32.9 us: 1.52x faster                                                    |
| deltablue               | 7.39 ms                                                | 3.24 ms: 2.28x faster                                                    |
| django_template         | 46.3 ms                                                | 32.5 ms: 1.42x faster                                                    |
| docutils                | 3.18 sec                                               | 2.55 sec: 1.25x faster                                                   |
| dulwich_log             | 75.5 ms                                                | 62.5 ms: 1.21x faster                                                    |
| fannkuch                | 477 ms                                                 | 366 ms: 1.30x faster                                                     |
| float                   | 108 ms                                                 | 73.2 ms: 1.47x faster                                                    |
| generators              | 75.8 ms                                                | 74.8 ms: 1.01x faster                                                    |
| genshi_text             | 30.6 ms                                                | 20.5 ms: 1.49x faster                                                    |
| genshi_xml              | 63.6 ms                                                | 47.4 ms: 1.34x faster                                                    |
| go                      | 226 ms                                                 | 132 ms: 1.72x faster                                                     |
| hexiom                  | 9.42 ms                                                | 6.10 ms: 1.54x faster                                                    |
| html5lib                | 85.8 ms                                                | 59.8 ms: 1.43x faster                                                    |
| json                    | 5.35 ms                                                | 5.03 ms: 1.06x faster                                                    |
| json_dumps              | 13.5 ms                                                | 9.32 ms: 1.45x faster                                                    |
| json_loads              | 28.9 us                                                | 24.1 us: 1.20x faster                                                    |
| logging_format          | 8.92 us                                                | 6.22 us: 1.44x faster                                                    |
| logging_silent          | 173 ns                                                 | 91.2 ns: 1.90x faster                                                    |
| logging_simple          | 8.06 us                                                | 5.63 us: 1.43x faster                                                    |
| mako                    | 14.3 ms                                                | 9.51 ms: 1.50x faster                                                    |
| mdp                     | 2.82 sec                                               | 2.71 sec: 1.04x faster                                                   |
| meteor_contest          | 114 ms                                                 | 108 ms: 1.06x faster                                                     |
| mypy                    | 1.01 sec                                               | 810 ms: 1.25x faster                                                     |
| nbody                   | 136 ms                                                 | 94.7 ms: 1.44x faster                                                    |
| nqueens                 | 99.3 ms                                                | 78.4 ms: 1.27x faster                                                    |
| pathlib                 | 20.0 ms                                                | 17.7 ms: 1.13x faster                                                    |
| pickle_dict             | 28.3 us                                                | 31.2 us: 1.10x slower                                                    |
| pickle_list             | 4.50 us                                                | 4.11 us: 1.10x faster                                                    |
| pickle_pure_python      | 453 us                                                 | 278 us: 1.63x faster                                                     |
| pidigits                | 190 ms                                                 | 193 ms: 1.01x slower                                                     |
| pprint_safe_repr        | 943 ms                                                 | 666 ms: 1.42x faster                                                     |
| pprint_pformat          | 1.97 sec                                               | 1.37 sec: 1.44x faster                                                   |
| pycparser               | 1.51 sec                                               | 1.10 sec: 1.37x faster                                                   |
| pyflate                 | 675 ms                                                 | 397 ms: 1.70x faster                                                     |
| python_startup          | 13.9 ms                                                | 8.56 ms: 1.63x faster                                                    |
| python_startup_no_site  | 5.76 ms                                                | 6.12 ms: 1.06x slower                                                    |
| raytrace                | 461 ms                                                 | 279 ms: 1.65x faster                                                     |
| regex_compile           | 174 ms                                                 | 131 ms: 1.33x faster                                                     |
| regex_dna               | 214 ms                                                 | 204 ms: 1.05x faster                                                     |
| regex_effbot            | 3.21 ms                                                | 3.43 ms: 1.07x slower                                                    |
| regex_v8                | 25.0 ms                                                | 21.9 ms: 1.14x faster                                                    |
| richards                | 71.4 ms                                                | 41.9 ms: 1.70x faster                                                    |
| scimark_fft             | 414 ms                                                 | 316 ms: 1.31x faster                                                     |
| scimark_lu              | 158 ms                                                 | 107 ms: 1.48x faster                                                     |
| scimark_monte_carlo     | 105 ms                                                 | 65.9 ms: 1.59x faster                                                    |
| scimark_sor             | 193 ms                                                 | 107 ms: 1.81x faster                                                     |
| scimark_sparse_mat_mult | 5.48 ms                                                | 4.27 ms: 1.28x faster                                                    |
| spectral_norm           | 148 ms                                                 | 95.8 ms: 1.55x faster                                                    |
| sqlglot_parse           | 2.04 ms                                                | 1.42 ms: 1.43x faster                                                    |
| sqlglot_transpile       | 2.42 ms                                                | 1.71 ms: 1.41x faster                                                    |
| sqlglot_optimize        | 65.3 ms                                                | 50.6 ms: 1.29x faster                                                    |
| sqlglot_normalize       | 135 ms                                                 | 104 ms: 1.30x faster                                                     |
| sqlite_synth            | 2.90 us                                                | 2.58 us: 1.12x faster                                                    |
| sympy_expand            | 537 ms                                                 | 453 ms: 1.19x faster                                                     |
| sympy_integrate         | 23.9 ms                                                | 20.5 ms: 1.17x faster                                                    |
| sympy_sum               | 183 ms                                                 | 164 ms: 1.12x faster                                                     |
| sympy_str               | 324 ms                                                 | 283 ms: 1.14x faster                                                     |
| telco                   | 6.68 ms                                                | 6.24 ms: 1.07x faster                                                    |
| thrift                  | 1.03 ms                                                | 750 us: 1.38x faster                                                     |
| unpack_sequence         | 59.5 ns                                                | 42.1 ns: 1.41x faster                                                    |
| unpickle                | 14.3 us                                                | 13.2 us: 1.08x faster                                                    |
| unpickle_pure_python    | 297 us                                                 | 198 us: 1.50x faster                                                     |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.10x faster                                                     |
| xml_etree_iterparse     | 110 ms                                                 | 107 ms: 1.03x faster                                                     |
| xml_etree_generate      | 93.3 ms                                                | 78.1 ms: 1.19x faster                                                    |
| xml_etree_process       | 74.5 ms                                                | 54.0 ms: 1.38x faster                                                    |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                             |

Benchmark hidden because not significant (3): bench_mp_pool, pickle, unpickle_list
Ignored benchmarks (7) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20221222-3.12.0a3+-79daf93/bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-79daf93.json: djangocms
