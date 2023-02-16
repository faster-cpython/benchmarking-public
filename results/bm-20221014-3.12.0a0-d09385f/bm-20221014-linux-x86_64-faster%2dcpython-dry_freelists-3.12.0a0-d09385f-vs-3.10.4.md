
# Results vs. 3.10.4

- fork: faster-cpython
- ref: dry_freelists
- machine: linux-x86_64
- commit hash: d09385f
- commit date: 2022-10-14
- overall geometric mean: 1.29x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221014-linux-x86_64-faster%2dcpython-dry_freelists-3.12.0a0-d09385f |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 248 ms: 1.35x faster                                                     |
| chameleon      | 9.17 ms                                                | 6.46 ms: 1.42x faster                                                    |
| docutils       | 3.18 sec                                               | 2.50 sec: 1.27x faster                                                   |
| html5lib       | 85.9 ms                                                | 59.6 ms: 1.44x faster                                                    |
| tornado_http   | 128 ms                                                 | 92.8 ms: 1.38x faster                                                    |
| Geometric mean | (ref)                                                  | 1.37x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221014-linux-x86_64-faster%2dcpython-dry_freelists-3.12.0a0-d09385f |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 144 ms                                                 | 95.2 ms: 1.51x faster                                                    |
| float          | 109 ms                                                 | 72.1 ms: 1.51x faster                                                    |
| pidigits       | 190 ms                                                 | 206 ms: 1.09x slower                                                     |
| Geometric mean | (ref)                                                  | 1.28x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221014-linux-x86_64-faster%2dcpython-dry_freelists-3.12.0a0-d09385f |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 127 ms: 1.40x faster                                                     |
| regex_v8       | 25.0 ms                                                | 22.3 ms: 1.12x faster                                                    |
| regex_dna      | 214 ms                                                 | 218 ms: 1.02x slower                                                     |
| regex_effbot   | 3.19 ms                                                | 3.43 ms: 1.07x slower                                                    |
| Geometric mean | (ref)                                                  | 1.09x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221014-linux-x86_64-faster%2dcpython-dry_freelists-3.12.0a0-d09385f |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 287 us: 1.58x faster                                                     |
| unpickle_pure_python | 302 us                                                 | 203 us: 1.49x faster                                                     |
| json_dumps           | 13.4 ms                                                | 9.30 ms: 1.45x faster                                                    |
| xml_etree_process    | 74.5 ms                                                | 53.9 ms: 1.38x faster                                                    |
| xml_etree_generate   | 93.8 ms                                                | 75.6 ms: 1.24x faster                                                    |
| json_loads           | 28.7 us                                                | 23.4 us: 1.22x faster                                                    |
| pickle_list          | 4.72 us                                                | 4.10 us: 1.15x faster                                                    |
| xml_etree_iterparse  | 111 ms                                                 | 102 ms: 1.09x faster                                                     |
| unpickle             | 14.2 us                                                | 13.1 us: 1.08x faster                                                    |
| xml_etree_parse      | 163 ms                                                 | 158 ms: 1.03x faster                                                     |
| pickle               | 10.2 us                                                | 10.3 us: 1.01x slower                                                    |
| pickle_dict          | 27.6 us                                                | 31.1 us: 1.13x slower                                                    |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                             |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221014-linux-x86_64-faster%2dcpython-dry_freelists-3.12.0a0-d09385f |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.41 ms: 1.68x faster                                                    |
| python_startup_no_site | 5.78 ms                                                | 5.94 ms: 1.03x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.28x faster                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221014-linux-x86_64-faster%2dcpython-dry_freelists-3.12.0a0-d09385f |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                | 9.89 ms: 1.48x faster                                                    |
| genshi_text     | 30.6 ms                                                | 20.8 ms: 1.47x faster                                                    |
| django_template | 46.3 ms                                                | 32.5 ms: 1.42x faster                                                    |
| genshi_xml      | 63.7 ms                                                | 49.1 ms: 1.30x faster                                                    |
| Geometric mean  | (ref)                                                  | 1.42x faster                                                             |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221014-linux-x86_64-faster%2dcpython-dry_freelists-3.12.0a0-d09385f |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| deltablue               | 7.28 ms                                                | 3.27 ms: 2.23x faster                                                    |
| logging_silent          | 176 ns                                                 | 92.5 ns: 1.91x faster                                                    |
| scimark_sor             | 197 ms                                                 | 108 ms: 1.83x faster                                                     |
| richards                | 75.2 ms                                                | 42.3 ms: 1.78x faster                                                    |
| go                      | 226 ms                                                 | 131 ms: 1.72x faster                                                     |
| pyflate                 | 676 ms                                                 | 400 ms: 1.69x faster                                                     |
| python_startup          | 14.1 ms                                                | 8.41 ms: 1.68x faster                                                    |
| scimark_monte_carlo     | 109 ms                                                 | 65.9 ms: 1.65x faster                                                    |
| raytrace                | 467 ms                                                 | 290 ms: 1.61x faster                                                     |
| chaos                   | 106 ms                                                 | 66.2 ms: 1.59x faster                                                    |
| pickle_pure_python      | 452 us                                                 | 287 us: 1.58x faster                                                     |
| hexiom                  | 9.43 ms                                                | 6.08 ms: 1.55x faster                                                    |
| crypto_pyaes            | 117 ms                                                 | 75.9 ms: 1.54x faster                                                    |
| sqlglot_parse           | 2.04 ms                                                | 1.34 ms: 1.52x faster                                                    |
| nbody                   | 144 ms                                                 | 95.2 ms: 1.51x faster                                                    |
| float                   | 109 ms                                                 | 72.1 ms: 1.51x faster                                                    |
| deepcopy_memo           | 51.7 us                                                | 34.7 us: 1.49x faster                                                    |
| unpickle_pure_python    | 302 us                                                 | 203 us: 1.49x faster                                                     |
| sqlglot_transpile       | 2.43 ms                                                | 1.63 ms: 1.49x faster                                                    |
| mako                    | 14.7 ms                                                | 9.89 ms: 1.48x faster                                                    |
| genshi_text             | 30.6 ms                                                | 20.8 ms: 1.47x faster                                                    |
| spectral_norm           | 150 ms                                                 | 102 ms: 1.47x faster                                                     |
| scimark_lu              | 161 ms                                                 | 110 ms: 1.47x faster                                                     |
| json_dumps              | 13.4 ms                                                | 9.30 ms: 1.45x faster                                                    |
| html5lib                | 85.9 ms                                                | 59.6 ms: 1.44x faster                                                    |
| pprint_pformat          | 1.98 sec                                               | 1.38 sec: 1.44x faster                                                   |
| django_template         | 46.3 ms                                                | 32.5 ms: 1.42x faster                                                    |
| pprint_safe_repr        | 953 ms                                                 | 670 ms: 1.42x faster                                                     |
| chameleon               | 9.17 ms                                                | 6.46 ms: 1.42x faster                                                    |
| logging_simple          | 8.10 us                                                | 5.76 us: 1.41x faster                                                    |
| regex_compile           | 177 ms                                                 | 127 ms: 1.40x faster                                                     |
| thrift                  | 1.03 ms                                                | 742 us: 1.39x faster                                                     |
| logging_format          | 8.85 us                                                | 6.37 us: 1.39x faster                                                    |
| async_tree_none         | 711 ms                                                 | 514 ms: 1.38x faster                                                     |
| xml_etree_process       | 74.5 ms                                                | 53.9 ms: 1.38x faster                                                    |
| tornado_http            | 128 ms                                                 | 92.8 ms: 1.38x faster                                                    |
| pycparser               | 1.53 sec                                               | 1.11 sec: 1.38x faster                                                   |
| async_tree_io           | 1.78 sec                                               | 1.31 sec: 1.35x faster                                                   |
| aiohttp                 | 1.34 ms                                                | 991 us: 1.35x faster                                                     |
| 2to3                    | 335 ms                                                 | 248 ms: 1.35x faster                                                     |
| unpack_sequence         | 59.4 ns                                                | 44.0 ns: 1.35x faster                                                    |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.05 ms: 1.35x faster                                                    |
| async_tree_memoization  | 855 ms                                                 | 636 ms: 1.35x faster                                                     |
| scimark_fft             | 421 ms                                                 | 315 ms: 1.34x faster                                                     |
| gunicorn                | 1.43 ms                                                | 1.07 ms: 1.34x faster                                                    |
| fannkuch                | 488 ms                                                 | 366 ms: 1.33x faster                                                     |
| deepcopy                | 438 us                                                 | 330 us: 1.33x faster                                                     |
| async_tree_cpu_io_mixed | 949 ms                                                 | 724 ms: 1.31x faster                                                     |
| deepcopy_reduce         | 3.79 us                                                | 2.92 us: 1.30x faster                                                    |
| genshi_xml              | 63.7 ms                                                | 49.1 ms: 1.30x faster                                                    |
| coroutines              | 31.6 ms                                                | 24.5 ms: 1.29x faster                                                    |
| sqlalchemy_imperative   | 21.5 ms                                                | 16.7 ms: 1.28x faster                                                    |
| sqlglot_normalize       | 134 ms                                                 | 105 ms: 1.28x faster                                                     |
| docutils                | 3.18 sec                                               | 2.50 sec: 1.27x faster                                                   |
| nqueens                 | 100 ms                                                 | 78.9 ms: 1.27x faster                                                    |
| sqlglot_optimize        | 65.2 ms                                                | 51.5 ms: 1.27x faster                                                    |
| sqlalchemy_declarative  | 165 ms                                                 | 133 ms: 1.24x faster                                                     |
| xml_etree_generate      | 93.8 ms                                                | 75.6 ms: 1.24x faster                                                    |
| json_loads              | 28.7 us                                                | 23.4 us: 1.22x faster                                                    |
| async_generators        | 426 ms                                                 | 349 ms: 1.22x faster                                                     |
| bench_thread_pool       | 946 us                                                 | 782 us: 1.21x faster                                                     |
| dulwich_log             | 75.8 ms                                                | 62.8 ms: 1.21x faster                                                    |
| json                    | 5.35 ms                                                | 4.48 ms: 1.19x faster                                                    |
| sympy_integrate         | 24.0 ms                                                | 20.3 ms: 1.18x faster                                                    |
| sympy_expand            | 534 ms                                                 | 453 ms: 1.18x faster                                                     |
| pylint                  | 532 ms                                                 | 453 ms: 1.17x faster                                                     |
| sympy_str               | 325 ms                                                 | 280 ms: 1.16x faster                                                     |
| pickle_list             | 4.72 us                                                | 4.10 us: 1.15x faster                                                    |
| create_gc_cycles        | 1.65 ms                                                | 1.44 ms: 1.14x faster                                                    |
| sqlite_synth            | 2.92 us                                                | 2.56 us: 1.14x faster                                                    |
| djangocms               | 36.9 us                                                | 32.6 us: 1.13x faster                                                    |
| sympy_sum               | 183 ms                                                 | 162 ms: 1.13x faster                                                     |
| regex_v8                | 25.0 ms                                                | 22.3 ms: 1.12x faster                                                    |
| pathlib                 | 20.0 ms                                                | 17.8 ms: 1.12x faster                                                    |
| xml_etree_iterparse     | 111 ms                                                 | 102 ms: 1.09x faster                                                     |
| meteor_contest          | 114 ms                                                 | 105 ms: 1.09x faster                                                     |
| unpickle                | 14.2 us                                                | 13.1 us: 1.08x faster                                                    |
| mdp                     | 2.74 sec                                               | 2.59 sec: 1.06x faster                                                   |
| asyncio_tcp             | 914 ms                                                 | 872 ms: 1.05x faster                                                     |
| xml_etree_parse         | 163 ms                                                 | 158 ms: 1.03x faster                                                     |
| telco                   | 6.73 ms                                                | 6.58 ms: 1.02x faster                                                    |
| generators              | 76.4 ms                                                | 75.4 ms: 1.01x faster                                                    |
| pickle                  | 10.2 us                                                | 10.3 us: 1.01x slower                                                    |
| regex_dna               | 214 ms                                                 | 218 ms: 1.02x slower                                                     |
| python_startup_no_site  | 5.78 ms                                                | 5.94 ms: 1.03x slower                                                    |
| regex_effbot            | 3.19 ms                                                | 3.43 ms: 1.07x slower                                                    |
| pidigits                | 190 ms                                                 | 206 ms: 1.09x slower                                                     |
| pickle_dict             | 27.6 us                                                | 31.1 us: 1.13x slower                                                    |
| dask                    | 436 ms                                                 | 496 ms: 1.14x slower                                                     |
| gc_traversal            | 3.53 ms                                                | 4.03 ms: 1.14x slower                                                    |
| coverage                | 74.7 ms                                                | 98.3 ms: 1.31x slower                                                    |
| Geometric mean          | (ref)                                                  | 1.29x faster                                                             |

Benchmark hidden because not significant (2): bench_mp_pool, unpickle_list
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, mypy2
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20221014-3.12.0a0-d09385f/bm-20221014-linux-x86_64-faster%2dcpython-dry_freelists-3.12.0a0-d09385f.json: mypy
