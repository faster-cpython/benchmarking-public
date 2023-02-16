
# Results vs. 3.10.4

- fork: brandtbucher
- ref: scan_small_dicts
- machine: linux-x86_64
- commit hash: 79daf93
- commit date: 2022-12-22
- overall geometric mean: 1.30x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-79daf93 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 253 ms: 1.33x faster                                                     |
| chameleon      | 9.17 ms                                                | 6.54 ms: 1.40x faster                                                    |
| docutils       | 3.18 sec                                               | 2.55 sec: 1.25x faster                                                   |
| html5lib       | 85.9 ms                                                | 59.8 ms: 1.43x faster                                                    |
| Geometric mean | (ref)                                                  | 1.35x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-79daf93 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 144 ms                                                 | 94.7 ms: 1.52x faster                                                    |
| float          | 109 ms                                                 | 73.2 ms: 1.49x faster                                                    |
| pidigits       | 190 ms                                                 | 193 ms: 1.01x slower                                                     |
| Geometric mean | (ref)                                                  | 1.31x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-79daf93 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 131 ms: 1.36x faster                                                     |
| regex_v8       | 25.0 ms                                                | 21.9 ms: 1.14x faster                                                    |
| regex_dna      | 214 ms                                                 | 204 ms: 1.05x faster                                                     |
| regex_effbot   | 3.19 ms                                                | 3.43 ms: 1.08x slower                                                    |
| Geometric mean | (ref)                                                  | 1.11x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-79daf93 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 278 us: 1.62x faster                                                     |
| unpickle_pure_python | 302 us                                                 | 198 us: 1.52x faster                                                     |
| json_dumps           | 13.4 ms                                                | 9.32 ms: 1.44x faster                                                    |
| xml_etree_process    | 74.5 ms                                                | 54.0 ms: 1.38x faster                                                    |
| xml_etree_generate   | 93.8 ms                                                | 78.1 ms: 1.20x faster                                                    |
| json_loads           | 28.7 us                                                | 24.1 us: 1.19x faster                                                    |
| pickle_list          | 4.72 us                                                | 4.11 us: 1.15x faster                                                    |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.10x faster                                                     |
| unpickle             | 14.2 us                                                | 13.2 us: 1.07x faster                                                    |
| xml_etree_iterparse  | 111 ms                                                 | 107 ms: 1.04x faster                                                     |
| unpickle_list        | 4.92 us                                                | 5.01 us: 1.02x slower                                                    |
| pickle_dict          | 27.6 us                                                | 31.2 us: 1.13x slower                                                    |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                             |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-79daf93 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.56 ms: 1.65x faster                                                    |
| python_startup_no_site | 5.78 ms                                                | 6.12 ms: 1.06x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.25x faster                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-79daf93 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                | 9.51 ms: 1.54x faster                                                    |
| genshi_text     | 30.6 ms                                                | 20.5 ms: 1.49x faster                                                    |
| django_template | 46.3 ms                                                | 32.5 ms: 1.43x faster                                                    |
| genshi_xml      | 63.7 ms                                                | 47.4 ms: 1.34x faster                                                    |
| Geometric mean  | (ref)                                                  | 1.45x faster                                                             |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-79daf93 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| deltablue               | 7.28 ms                                                | 3.24 ms: 2.25x faster                                                    |
| logging_silent          | 176 ns                                                 | 91.2 ns: 1.93x faster                                                    |
| scimark_sor             | 197 ms                                                 | 107 ms: 1.84x faster                                                     |
| richards                | 75.2 ms                                                | 41.9 ms: 1.79x faster                                                    |
| go                      | 226 ms                                                 | 132 ms: 1.71x faster                                                     |
| pyflate                 | 676 ms                                                 | 397 ms: 1.70x faster                                                     |
| raytrace                | 467 ms                                                 | 279 ms: 1.67x faster                                                     |
| scimark_monte_carlo     | 109 ms                                                 | 65.9 ms: 1.65x faster                                                    |
| python_startup          | 14.1 ms                                                | 8.56 ms: 1.65x faster                                                    |
| pickle_pure_python      | 452 us                                                 | 278 us: 1.62x faster                                                     |
| chaos                   | 106 ms                                                 | 66.4 ms: 1.59x faster                                                    |
| deepcopy_memo           | 51.7 us                                                | 32.9 us: 1.57x faster                                                    |
| spectral_norm           | 150 ms                                                 | 95.8 ms: 1.56x faster                                                    |
| hexiom                  | 9.43 ms                                                | 6.10 ms: 1.55x faster                                                    |
| mako                    | 14.7 ms                                                | 9.51 ms: 1.54x faster                                                    |
| crypto_pyaes            | 117 ms                                                 | 75.9 ms: 1.54x faster                                                    |
| unpickle_pure_python    | 302 us                                                 | 198 us: 1.52x faster                                                     |
| nbody                   | 144 ms                                                 | 94.7 ms: 1.52x faster                                                    |
| scimark_lu              | 161 ms                                                 | 107 ms: 1.51x faster                                                     |
| genshi_text             | 30.6 ms                                                | 20.5 ms: 1.49x faster                                                    |
| float                   | 109 ms                                                 | 73.2 ms: 1.49x faster                                                    |
| pprint_pformat          | 1.98 sec                                               | 1.37 sec: 1.45x faster                                                   |
| json_dumps              | 13.4 ms                                                | 9.32 ms: 1.44x faster                                                    |
| sqlglot_parse           | 2.04 ms                                                | 1.42 ms: 1.44x faster                                                    |
| logging_simple          | 8.10 us                                                | 5.63 us: 1.44x faster                                                    |
| html5lib                | 85.9 ms                                                | 59.8 ms: 1.43x faster                                                    |
| pprint_safe_repr        | 953 ms                                                 | 666 ms: 1.43x faster                                                     |
| django_template         | 46.3 ms                                                | 32.5 ms: 1.43x faster                                                    |
| logging_format          | 8.85 us                                                | 6.22 us: 1.42x faster                                                    |
| sqlglot_transpile       | 2.43 ms                                                | 1.71 ms: 1.42x faster                                                    |
| unpack_sequence         | 59.4 ns                                                | 42.1 ns: 1.41x faster                                                    |
| chameleon               | 9.17 ms                                                | 6.54 ms: 1.40x faster                                                    |
| pycparser               | 1.53 sec                                               | 1.10 sec: 1.39x faster                                                   |
| xml_etree_process       | 74.5 ms                                                | 54.0 ms: 1.38x faster                                                    |
| thrift                  | 1.03 ms                                                | 750 us: 1.38x faster                                                     |
| deepcopy                | 438 us                                                 | 322 us: 1.36x faster                                                     |
| regex_compile           | 177 ms                                                 | 131 ms: 1.36x faster                                                     |
| genshi_xml              | 63.7 ms                                                | 47.4 ms: 1.34x faster                                                    |
| scimark_fft             | 421 ms                                                 | 316 ms: 1.33x faster                                                     |
| async_tree_io           | 1.78 sec                                               | 1.34 sec: 1.33x faster                                                   |
| fannkuch                | 488 ms                                                 | 366 ms: 1.33x faster                                                     |
| 2to3                    | 335 ms                                                 | 253 ms: 1.33x faster                                                     |
| async_tree_none         | 711 ms                                                 | 537 ms: 1.32x faster                                                     |
| async_tree_memoization  | 855 ms                                                 | 651 ms: 1.31x faster                                                     |
| deepcopy_reduce         | 3.79 us                                                | 2.89 us: 1.31x faster                                                    |
| sqlglot_normalize       | 134 ms                                                 | 104 ms: 1.29x faster                                                     |
| sqlglot_optimize        | 65.2 ms                                                | 50.6 ms: 1.29x faster                                                    |
| coroutines              | 31.6 ms                                                | 24.8 ms: 1.28x faster                                                    |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.27 ms: 1.28x faster                                                    |
| nqueens                 | 100 ms                                                 | 78.4 ms: 1.28x faster                                                    |
| docutils                | 3.18 sec                                               | 2.55 sec: 1.25x faster                                                   |
| async_tree_cpu_io_mixed | 949 ms                                                 | 768 ms: 1.24x faster                                                     |
| async_generators        | 426 ms                                                 | 349 ms: 1.22x faster                                                     |
| bench_thread_pool       | 946 us                                                 | 778 us: 1.22x faster                                                     |
| dulwich_log             | 75.8 ms                                                | 62.5 ms: 1.21x faster                                                    |
| xml_etree_generate      | 93.8 ms                                                | 78.1 ms: 1.20x faster                                                    |
| json_loads              | 28.7 us                                                | 24.1 us: 1.19x faster                                                    |
| sympy_expand            | 534 ms                                                 | 453 ms: 1.18x faster                                                     |
| sympy_integrate         | 24.0 ms                                                | 20.5 ms: 1.18x faster                                                    |
| pickle_list             | 4.72 us                                                | 4.11 us: 1.15x faster                                                    |
| sympy_str               | 325 ms                                                 | 283 ms: 1.15x faster                                                     |
| regex_v8                | 25.0 ms                                                | 21.9 ms: 1.14x faster                                                    |
| sqlite_synth            | 2.92 us                                                | 2.58 us: 1.13x faster                                                    |
| pathlib                 | 20.0 ms                                                | 17.7 ms: 1.13x faster                                                    |
| djangocms               | 36.9 us                                                | 32.8 us: 1.12x faster                                                    |
| sympy_sum               | 183 ms                                                 | 164 ms: 1.12x faster                                                     |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.10x faster                                                     |
| telco                   | 6.73 ms                                                | 6.24 ms: 1.08x faster                                                    |
| unpickle                | 14.2 us                                                | 13.2 us: 1.07x faster                                                    |
| json                    | 5.35 ms                                                | 5.03 ms: 1.06x faster                                                    |
| meteor_contest          | 114 ms                                                 | 108 ms: 1.06x faster                                                     |
| regex_dna               | 214 ms                                                 | 204 ms: 1.05x faster                                                     |
| xml_etree_iterparse     | 111 ms                                                 | 107 ms: 1.04x faster                                                     |
| generators              | 76.4 ms                                                | 74.8 ms: 1.02x faster                                                    |
| mdp                     | 2.74 sec                                               | 2.71 sec: 1.01x faster                                                   |
| pidigits                | 190 ms                                                 | 193 ms: 1.01x slower                                                     |
| unpickle_list           | 4.92 us                                                | 5.01 us: 1.02x slower                                                    |
| python_startup_no_site  | 5.78 ms                                                | 6.12 ms: 1.06x slower                                                    |
| regex_effbot            | 3.19 ms                                                | 3.43 ms: 1.08x slower                                                    |
| pickle_dict             | 27.6 us                                                | 31.2 us: 1.13x slower                                                    |
| coverage                | 74.7 ms                                                | 97.5 ms: 1.30x slower                                                    |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                             |

Benchmark hidden because not significant (2): pickle, bench_mp_pool
Ignored benchmarks (12) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, create_gc_cycles, dask, flaskblogging, gc_traversal, gunicorn, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20221222-3.12.0a3+-79daf93/bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-79daf93.json: mypy
