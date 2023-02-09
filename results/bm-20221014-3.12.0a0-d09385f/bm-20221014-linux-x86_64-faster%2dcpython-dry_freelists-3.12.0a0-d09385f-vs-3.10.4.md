
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
| 2to3           | 332 ms                                                 | 248 ms: 1.34x faster                                                     |
| chameleon      | 8.86 ms                                                | 6.46 ms: 1.37x faster                                                    |
| docutils       | 3.18 sec                                               | 2.50 sec: 1.27x faster                                                   |
| html5lib       | 85.8 ms                                                | 59.6 ms: 1.44x faster                                                    |
| tornado_http   | 128 ms                                                 | 92.8 ms: 1.38x faster                                                    |
| Geometric mean | (ref)                                                  | 1.36x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221014-linux-x86_64-faster%2dcpython-dry_freelists-3.12.0a0-d09385f |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 108 ms                                                 | 72.1 ms: 1.49x faster                                                    |
| nbody          | 136 ms                                                 | 95.2 ms: 1.43x faster                                                    |
| pidigits       | 190 ms                                                 | 206 ms: 1.08x slower                                                     |
| Geometric mean | (ref)                                                  | 1.25x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221014-linux-x86_64-faster%2dcpython-dry_freelists-3.12.0a0-d09385f |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 174 ms                                                 | 127 ms: 1.37x faster                                                     |
| regex_v8       | 25.0 ms                                                | 22.3 ms: 1.12x faster                                                    |
| regex_dna      | 214 ms                                                 | 218 ms: 1.02x slower                                                     |
| regex_effbot   | 3.21 ms                                                | 3.43 ms: 1.07x slower                                                    |
| Geometric mean | (ref)                                                  | 1.09x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221014-linux-x86_64-faster%2dcpython-dry_freelists-3.12.0a0-d09385f |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| pickle_pure_python   | 453 us                                                 | 287 us: 1.58x faster                                                     |
| unpickle_pure_python | 297 us                                                 | 203 us: 1.46x faster                                                     |
| json_dumps           | 13.5 ms                                                | 9.30 ms: 1.45x faster                                                    |
| xml_etree_process    | 74.5 ms                                                | 53.9 ms: 1.38x faster                                                    |
| xml_etree_generate   | 93.3 ms                                                | 75.6 ms: 1.23x faster                                                    |
| json_loads           | 28.9 us                                                | 23.4 us: 1.23x faster                                                    |
| pickle_list          | 4.50 us                                                | 4.10 us: 1.10x faster                                                    |
| unpickle             | 14.3 us                                                | 13.1 us: 1.09x faster                                                    |
| xml_etree_iterparse  | 110 ms                                                 | 102 ms: 1.08x faster                                                     |
| xml_etree_parse      | 163 ms                                                 | 158 ms: 1.04x faster                                                     |
| pickle               | 10.1 us                                                | 10.3 us: 1.01x slower                                                    |
| pickle_dict          | 28.3 us                                                | 31.1 us: 1.10x slower                                                    |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                             |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221014-linux-x86_64-faster%2dcpython-dry_freelists-3.12.0a0-d09385f |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 13.9 ms                                                | 8.41 ms: 1.66x faster                                                    |
| python_startup_no_site | 5.76 ms                                                | 5.94 ms: 1.03x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.27x faster                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221014-linux-x86_64-faster%2dcpython-dry_freelists-3.12.0a0-d09385f |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text     | 30.6 ms                                                | 20.8 ms: 1.47x faster                                                    |
| mako            | 14.3 ms                                                | 9.89 ms: 1.44x faster                                                    |
| django_template | 46.3 ms                                                | 32.5 ms: 1.42x faster                                                    |
| genshi_xml      | 63.6 ms                                                | 49.1 ms: 1.29x faster                                                    |
| Geometric mean  | (ref)                                                  | 1.41x faster                                                             |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221014-linux-x86_64-faster%2dcpython-dry_freelists-3.12.0a0-d09385f |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| deltablue               | 7.39 ms                                                | 3.27 ms: 2.26x faster                                                    |
| logging_silent          | 173 ns                                                 | 92.5 ns: 1.87x faster                                                    |
| scimark_sor             | 193 ms                                                 | 108 ms: 1.79x faster                                                     |
| go                      | 226 ms                                                 | 131 ms: 1.73x faster                                                     |
| pyflate                 | 675 ms                                                 | 400 ms: 1.69x faster                                                     |
| richards                | 71.4 ms                                                | 42.3 ms: 1.69x faster                                                    |
| python_startup          | 13.9 ms                                                | 8.41 ms: 1.66x faster                                                    |
| raytrace                | 461 ms                                                 | 290 ms: 1.59x faster                                                     |
| scimark_monte_carlo     | 105 ms                                                 | 65.9 ms: 1.59x faster                                                    |
| mypy                    | 1.01 sec                                               | 639 ms: 1.59x faster                                                     |
| pickle_pure_python      | 453 us                                                 | 287 us: 1.58x faster                                                     |
| chaos                   | 104 ms                                                 | 66.2 ms: 1.57x faster                                                    |
| hexiom                  | 9.42 ms                                                | 6.08 ms: 1.55x faster                                                    |
| crypto_pyaes            | 118 ms                                                 | 75.9 ms: 1.55x faster                                                    |
| sqlglot_parse           | 2.04 ms                                                | 1.34 ms: 1.52x faster                                                    |
| float                   | 108 ms                                                 | 72.1 ms: 1.49x faster                                                    |
| sqlglot_transpile       | 2.42 ms                                                | 1.63 ms: 1.48x faster                                                    |
| genshi_text             | 30.6 ms                                                | 20.8 ms: 1.47x faster                                                    |
| unpickle_pure_python    | 297 us                                                 | 203 us: 1.46x faster                                                     |
| spectral_norm           | 148 ms                                                 | 102 ms: 1.46x faster                                                     |
| json_dumps              | 13.5 ms                                                | 9.30 ms: 1.45x faster                                                    |
| scimark_lu              | 158 ms                                                 | 110 ms: 1.44x faster                                                     |
| mako                    | 14.3 ms                                                | 9.89 ms: 1.44x faster                                                    |
| html5lib                | 85.8 ms                                                | 59.6 ms: 1.44x faster                                                    |
| deepcopy_memo           | 50.0 us                                                | 34.7 us: 1.44x faster                                                    |
| pprint_pformat          | 1.97 sec                                               | 1.38 sec: 1.43x faster                                                   |
| nbody                   | 136 ms                                                 | 95.2 ms: 1.43x faster                                                    |
| django_template         | 46.3 ms                                                | 32.5 ms: 1.42x faster                                                    |
| pprint_safe_repr        | 943 ms                                                 | 670 ms: 1.41x faster                                                     |
| logging_format          | 8.92 us                                                | 6.37 us: 1.40x faster                                                    |
| logging_simple          | 8.06 us                                                | 5.76 us: 1.40x faster                                                    |
| thrift                  | 1.03 ms                                                | 742 us: 1.39x faster                                                     |
| async_tree_none         | 713 ms                                                 | 514 ms: 1.39x faster                                                     |
| tornado_http            | 128 ms                                                 | 92.8 ms: 1.38x faster                                                    |
| xml_etree_process       | 74.5 ms                                                | 53.9 ms: 1.38x faster                                                    |
| chameleon               | 8.86 ms                                                | 6.46 ms: 1.37x faster                                                    |
| regex_compile           | 174 ms                                                 | 127 ms: 1.37x faster                                                     |
| pycparser               | 1.51 sec                                               | 1.11 sec: 1.36x faster                                                   |
| scimark_sparse_mat_mult | 5.48 ms                                                | 4.05 ms: 1.35x faster                                                    |
| unpack_sequence         | 59.5 ns                                                | 44.0 ns: 1.35x faster                                                    |
| async_tree_io           | 1.78 sec                                               | 1.31 sec: 1.35x faster                                                   |
| aiohttp                 | 1.34 ms                                                | 991 us: 1.35x faster                                                     |
| async_tree_memoization  | 854 ms                                                 | 636 ms: 1.34x faster                                                     |
| gunicorn                | 1.43 ms                                                | 1.07 ms: 1.34x faster                                                    |
| 2to3                    | 332 ms                                                 | 248 ms: 1.34x faster                                                     |
| scimark_fft             | 414 ms                                                 | 315 ms: 1.31x faster                                                     |
| async_tree_cpu_io_mixed | 949 ms                                                 | 724 ms: 1.31x faster                                                     |
| fannkuch                | 477 ms                                                 | 366 ms: 1.30x faster                                                     |
| deepcopy                | 429 us                                                 | 330 us: 1.30x faster                                                     |
| genshi_xml              | 63.6 ms                                                | 49.1 ms: 1.29x faster                                                    |
| coroutines              | 31.7 ms                                                | 24.5 ms: 1.29x faster                                                    |
| deepcopy_reduce         | 3.75 us                                                | 2.92 us: 1.29x faster                                                    |
| sqlglot_normalize       | 135 ms                                                 | 105 ms: 1.28x faster                                                     |
| docutils                | 3.18 sec                                               | 2.50 sec: 1.27x faster                                                   |
| sqlglot_optimize        | 65.3 ms                                                | 51.5 ms: 1.27x faster                                                    |
| nqueens                 | 99.3 ms                                                | 78.9 ms: 1.26x faster                                                    |
| sqlalchemy_imperative   | 21.0 ms                                                | 16.7 ms: 1.26x faster                                                    |
| sqlalchemy_declarative  | 165 ms                                                 | 133 ms: 1.25x faster                                                     |
| xml_etree_generate      | 93.3 ms                                                | 75.6 ms: 1.23x faster                                                    |
| json_loads              | 28.9 us                                                | 23.4 us: 1.23x faster                                                    |
| async_generators        | 428 ms                                                 | 349 ms: 1.23x faster                                                     |
| bench_thread_pool       | 943 us                                                 | 782 us: 1.21x faster                                                     |
| dulwich_log             | 75.5 ms                                                | 62.8 ms: 1.20x faster                                                    |
| json                    | 5.35 ms                                                | 4.48 ms: 1.20x faster                                                    |
| sympy_expand            | 537 ms                                                 | 453 ms: 1.19x faster                                                     |
| sympy_integrate         | 23.9 ms                                                | 20.3 ms: 1.18x faster                                                    |
| sympy_str               | 324 ms                                                 | 280 ms: 1.16x faster                                                     |
| pylint                  | 519 ms                                                 | 453 ms: 1.15x faster                                                     |
| sqlite_synth            | 2.90 us                                                | 2.56 us: 1.13x faster                                                    |
| sympy_sum               | 183 ms                                                 | 162 ms: 1.13x faster                                                     |
| pathlib                 | 20.0 ms                                                | 17.8 ms: 1.12x faster                                                    |
| regex_v8                | 25.0 ms                                                | 22.3 ms: 1.12x faster                                                    |
| pickle_list             | 4.50 us                                                | 4.10 us: 1.10x faster                                                    |
| unpickle                | 14.3 us                                                | 13.1 us: 1.09x faster                                                    |
| mdp                     | 2.82 sec                                               | 2.59 sec: 1.09x faster                                                   |
| meteor_contest          | 114 ms                                                 | 105 ms: 1.09x faster                                                     |
| xml_etree_iterparse     | 110 ms                                                 | 102 ms: 1.08x faster                                                     |
| xml_etree_parse         | 163 ms                                                 | 158 ms: 1.04x faster                                                     |
| telco                   | 6.68 ms                                                | 6.58 ms: 1.01x faster                                                    |
| generators              | 75.8 ms                                                | 75.4 ms: 1.01x faster                                                    |
| pickle                  | 10.1 us                                                | 10.3 us: 1.01x slower                                                    |
| regex_dna               | 214 ms                                                 | 218 ms: 1.02x slower                                                     |
| python_startup_no_site  | 5.76 ms                                                | 5.94 ms: 1.03x slower                                                    |
| regex_effbot            | 3.21 ms                                                | 3.43 ms: 1.07x slower                                                    |
| pidigits                | 190 ms                                                 | 206 ms: 1.08x slower                                                     |
| pickle_dict             | 28.3 us                                                | 31.1 us: 1.10x slower                                                    |
| coverage                | 75.3 ms                                                | 98.3 ms: 1.30x slower                                                    |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                             |

Benchmark hidden because not significant (2): unpickle_list, bench_mp_pool
Ignored benchmarks (1) of /home/mdboom/Work/builds/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging
Ignored benchmarks (5) of /home/mdboom/Work/builds/benchmarking/results/bm-20221014-3.12.0a0-d09385f/bm-20221014-linux-x86_64-faster%2dcpython-dry_freelists-3.12.0a0-d09385f.json: asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal
