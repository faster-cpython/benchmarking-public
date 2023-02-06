
# Results vs. 3.10.4

- fork: faster-cpython
- ref: dry_freelists
- machine: linux-x86_64
- commit hash: d09385f
- commit date: 2022-10-14
- overall geometric mean: 1.30x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221014-linux-x86_64-faster%2dcpython-dry_freelists-3.12.0a0-d09385f |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 332 ms                                                 | 246 ms: 1.35x faster                                                     |
| chameleon      | 8.86 ms                                                | 6.46 ms: 1.37x faster                                                    |
| docutils       | 3.18 sec                                               | 2.51 sec: 1.27x faster                                                   |
| html5lib       | 85.8 ms                                                | 59.8 ms: 1.43x faster                                                    |
| tornado_http   | 128 ms                                                 | 93.2 ms: 1.38x faster                                                    |
| Geometric mean | (ref)                                                  | 1.36x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221014-linux-x86_64-faster%2dcpython-dry_freelists-3.12.0a0-d09385f |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 108 ms                                                 | 71.8 ms: 1.50x faster                                                    |
| nbody          | 136 ms                                                 | 94.3 ms: 1.44x faster                                                    |
| pidigits       | 190 ms                                                 | 191 ms: 1.00x slower                                                     |
| Geometric mean | (ref)                                                  | 1.29x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221014-linux-x86_64-faster%2dcpython-dry_freelists-3.12.0a0-d09385f |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 174 ms                                                 | 129 ms: 1.35x faster                                                     |
| regex_v8       | 25.0 ms                                                | 21.8 ms: 1.15x faster                                                    |
| regex_dna      | 214 ms                                                 | 206 ms: 1.04x faster                                                     |
| regex_effbot   | 3.21 ms                                                | 3.63 ms: 1.13x slower                                                    |
| Geometric mean | (ref)                                                  | 1.09x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221014-linux-x86_64-faster%2dcpython-dry_freelists-3.12.0a0-d09385f |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| pickle_pure_python   | 453 us                                                 | 291 us: 1.56x faster                                                     |
| unpickle_pure_python | 297 us                                                 | 203 us: 1.46x faster                                                     |
| json_dumps           | 13.5 ms                                                | 9.42 ms: 1.43x faster                                                    |
| xml_etree_process    | 74.5 ms                                                | 53.9 ms: 1.38x faster                                                    |
| json_loads           | 28.9 us                                                | 23.5 us: 1.23x faster                                                    |
| xml_etree_generate   | 93.3 ms                                                | 76.4 ms: 1.22x faster                                                    |
| pickle_list          | 4.50 us                                                | 3.95 us: 1.14x faster                                                    |
| unpickle             | 14.3 us                                                | 13.0 us: 1.10x faster                                                    |
| xml_etree_iterparse  | 110 ms                                                 | 106 ms: 1.04x faster                                                     |
| xml_etree_parse      | 163 ms                                                 | 159 ms: 1.02x faster                                                     |
| unpickle_list        | 4.99 us                                                | 4.88 us: 1.02x faster                                                    |
| pickle_dict          | 28.3 us                                                | 30.0 us: 1.06x slower                                                    |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                             |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221014-linux-x86_64-faster%2dcpython-dry_freelists-3.12.0a0-d09385f |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 13.9 ms                                                | 8.43 ms: 1.65x faster                                                    |
| python_startup_no_site | 5.76 ms                                                | 5.95 ms: 1.03x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.27x faster                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221014-linux-x86_64-faster%2dcpython-dry_freelists-3.12.0a0-d09385f |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 14.3 ms                                                | 9.60 ms: 1.48x faster                                                    |
| genshi_text     | 30.6 ms                                                | 20.7 ms: 1.48x faster                                                    |
| django_template | 46.3 ms                                                | 32.2 ms: 1.44x faster                                                    |
| genshi_xml      | 63.6 ms                                                | 48.6 ms: 1.31x faster                                                    |
| Geometric mean  | (ref)                                                  | 1.43x faster                                                             |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221014-linux-x86_64-faster%2dcpython-dry_freelists-3.12.0a0-d09385f |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| deltablue               | 7.39 ms                                                | 3.29 ms: 2.24x faster                                                    |
| logging_silent          | 173 ns                                                 | 91.9 ns: 1.88x faster                                                    |
| scimark_sor             | 193 ms                                                 | 107 ms: 1.80x faster                                                     |
| go                      | 226 ms                                                 | 132 ms: 1.72x faster                                                     |
| pyflate                 | 675 ms                                                 | 397 ms: 1.70x faster                                                     |
| richards                | 71.4 ms                                                | 42.8 ms: 1.67x faster                                                    |
| python_startup          | 13.9 ms                                                | 8.43 ms: 1.65x faster                                                    |
| raytrace                | 461 ms                                                 | 282 ms: 1.63x faster                                                     |
| scimark_monte_carlo     | 105 ms                                                 | 66.1 ms: 1.58x faster                                                    |
| mypy                    | 1.01 sec                                               | 640 ms: 1.58x faster                                                     |
| pickle_pure_python      | 453 us                                                 | 291 us: 1.56x faster                                                     |
| crypto_pyaes            | 118 ms                                                 | 76.3 ms: 1.54x faster                                                    |
| chaos                   | 104 ms                                                 | 67.9 ms: 1.53x faster                                                    |
| hexiom                  | 9.42 ms                                                | 6.18 ms: 1.52x faster                                                    |
| sqlglot_parse           | 2.04 ms                                                | 1.34 ms: 1.51x faster                                                    |
| float                   | 108 ms                                                 | 71.8 ms: 1.50x faster                                                    |
| spectral_norm           | 148 ms                                                 | 99.0 ms: 1.50x faster                                                    |
| mako                    | 14.3 ms                                                | 9.60 ms: 1.48x faster                                                    |
| genshi_text             | 30.6 ms                                                | 20.7 ms: 1.48x faster                                                    |
| sqlglot_transpile       | 2.42 ms                                                | 1.64 ms: 1.48x faster                                                    |
| unpickle_pure_python    | 297 us                                                 | 203 us: 1.46x faster                                                     |
| deepcopy_memo           | 50.0 us                                                | 34.4 us: 1.45x faster                                                    |
| nbody                   | 136 ms                                                 | 94.3 ms: 1.44x faster                                                    |
| pprint_pformat          | 1.97 sec                                               | 1.37 sec: 1.44x faster                                                   |
| django_template         | 46.3 ms                                                | 32.2 ms: 1.44x faster                                                    |
| html5lib                | 85.8 ms                                                | 59.8 ms: 1.43x faster                                                    |
| json_dumps              | 13.5 ms                                                | 9.42 ms: 1.43x faster                                                    |
| logging_simple          | 8.06 us                                                | 5.67 us: 1.42x faster                                                    |
| logging_format          | 8.92 us                                                | 6.34 us: 1.41x faster                                                    |
| scimark_lu              | 158 ms                                                 | 113 ms: 1.41x faster                                                     |
| pprint_safe_repr        | 943 ms                                                 | 674 ms: 1.40x faster                                                     |
| thrift                  | 1.03 ms                                                | 746 us: 1.38x faster                                                     |
| xml_etree_process       | 74.5 ms                                                | 53.9 ms: 1.38x faster                                                    |
| async_tree_none         | 713 ms                                                 | 517 ms: 1.38x faster                                                     |
| tornado_http            | 128 ms                                                 | 93.2 ms: 1.38x faster                                                    |
| chameleon               | 8.86 ms                                                | 6.46 ms: 1.37x faster                                                    |
| pycparser               | 1.51 sec                                               | 1.11 sec: 1.36x faster                                                   |
| unpack_sequence         | 59.5 ns                                                | 43.8 ns: 1.36x faster                                                    |
| async_tree_io           | 1.78 sec                                               | 1.31 sec: 1.35x faster                                                   |
| regex_compile           | 174 ms                                                 | 129 ms: 1.35x faster                                                     |
| 2to3                    | 332 ms                                                 | 246 ms: 1.35x faster                                                     |
| async_tree_memoization  | 854 ms                                                 | 633 ms: 1.35x faster                                                     |
| aiohttp                 | 1.34 ms                                                | 993 us: 1.35x faster                                                     |
| gunicorn                | 1.43 ms                                                | 1.07 ms: 1.34x faster                                                    |
| genshi_xml              | 63.6 ms                                                | 48.6 ms: 1.31x faster                                                    |
| fannkuch                | 477 ms                                                 | 365 ms: 1.31x faster                                                     |
| scimark_sparse_mat_mult | 5.48 ms                                                | 4.22 ms: 1.30x faster                                                    |
| deepcopy_reduce         | 3.75 us                                                | 2.89 us: 1.30x faster                                                    |
| scimark_fft             | 414 ms                                                 | 320 ms: 1.29x faster                                                     |
| async_tree_cpu_io_mixed | 949 ms                                                 | 734 ms: 1.29x faster                                                     |
| sqlglot_normalize       | 135 ms                                                 | 105 ms: 1.29x faster                                                     |
| deepcopy                | 429 us                                                 | 336 us: 1.28x faster                                                     |
| docutils                | 3.18 sec                                               | 2.51 sec: 1.27x faster                                                   |
| sqlglot_optimize        | 65.3 ms                                                | 51.6 ms: 1.27x faster                                                    |
| nqueens                 | 99.3 ms                                                | 78.5 ms: 1.26x faster                                                    |
| sqlalchemy_imperative   | 21.0 ms                                                | 17.0 ms: 1.24x faster                                                    |
| sqlalchemy_declarative  | 165 ms                                                 | 134 ms: 1.24x faster                                                     |
| coroutines              | 31.7 ms                                                | 25.7 ms: 1.23x faster                                                    |
| json_loads              | 28.9 us                                                | 23.5 us: 1.23x faster                                                    |
| xml_etree_generate      | 93.3 ms                                                | 76.4 ms: 1.22x faster                                                    |
| dulwich_log             | 75.5 ms                                                | 62.5 ms: 1.21x faster                                                    |
| async_generators        | 428 ms                                                 | 355 ms: 1.21x faster                                                     |
| bench_thread_pool       | 943 us                                                 | 783 us: 1.20x faster                                                     |
| json                    | 5.35 ms                                                | 4.48 ms: 1.20x faster                                                    |
| sympy_expand            | 537 ms                                                 | 453 ms: 1.19x faster                                                     |
| sympy_integrate         | 23.9 ms                                                | 20.4 ms: 1.17x faster                                                    |
| sympy_str               | 324 ms                                                 | 282 ms: 1.15x faster                                                     |
| regex_v8                | 25.0 ms                                                | 21.8 ms: 1.15x faster                                                    |
| pickle_list             | 4.50 us                                                | 3.95 us: 1.14x faster                                                    |
| pylint                  | 519 ms                                                 | 456 ms: 1.14x faster                                                     |
| sympy_sum               | 183 ms                                                 | 163 ms: 1.13x faster                                                     |
| sqlite_synth            | 2.90 us                                                | 2.58 us: 1.13x faster                                                    |
| pathlib                 | 20.0 ms                                                | 18.1 ms: 1.11x faster                                                    |
| unpickle                | 14.3 us                                                | 13.0 us: 1.10x faster                                                    |
| meteor_contest          | 114 ms                                                 | 104 ms: 1.09x faster                                                     |
| telco                   | 6.68 ms                                                | 6.41 ms: 1.04x faster                                                    |
| mdp                     | 2.82 sec                                               | 2.71 sec: 1.04x faster                                                   |
| regex_dna               | 214 ms                                                 | 206 ms: 1.04x faster                                                     |
| xml_etree_iterparse     | 110 ms                                                 | 106 ms: 1.04x faster                                                     |
| generators              | 75.8 ms                                                | 73.3 ms: 1.03x faster                                                    |
| xml_etree_parse         | 163 ms                                                 | 159 ms: 1.02x faster                                                     |
| unpickle_list           | 4.99 us                                                | 4.88 us: 1.02x faster                                                    |
| pidigits                | 190 ms                                                 | 191 ms: 1.00x slower                                                     |
| python_startup_no_site  | 5.76 ms                                                | 5.95 ms: 1.03x slower                                                    |
| pickle_dict             | 28.3 us                                                | 30.0 us: 1.06x slower                                                    |
| regex_effbot            | 3.21 ms                                                | 3.63 ms: 1.13x slower                                                    |
| coverage                | 75.3 ms                                                | 98.9 ms: 1.31x slower                                                    |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                             |

Benchmark hidden because not significant (2): bench_mp_pool, pickle
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20221014-3.12.0a0-d09385f/bm-20221014-linux-x86_64-faster%2dcpython-dry_freelists-3.12.0a0-d09385f.json: asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal
