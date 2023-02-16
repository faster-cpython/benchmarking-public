
# Results vs. 3.11.0

- fork: faster-cpython
- ref: dry_freelists
- machine: linux-x86_64
- commit hash: d09385f
- commit date: 2022-10-14
- overall geometric mean: 1.03x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221014-linux-x86_64-faster%2dcpython-dry_freelists-3.12.0a0-d09385f |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 248 ms: 1.04x faster                                                     |
| chameleon      | 6.38 ms                                                | 6.46 ms: 1.01x slower                                                    |
| docutils       | 2.60 sec                                               | 2.50 sec: 1.04x faster                                                   |
| html5lib       | 64.8 ms                                                | 59.6 ms: 1.09x faster                                                    |
| tornado_http   | 96.5 ms                                                | 92.8 ms: 1.04x faster                                                    |
| Geometric mean | (ref)                                                  | 1.04x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221014-linux-x86_64-faster%2dcpython-dry_freelists-3.12.0a0-d09385f |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 76.8 ms                                                | 72.1 ms: 1.06x faster                                                    |
| pidigits       | 197 ms                                                 | 206 ms: 1.05x slower                                                     |
| nbody          | 90.0 ms                                                | 95.2 ms: 1.06x slower                                                    |
| Geometric mean | (ref)                                                  | 1.01x slower                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221014-linux-x86_64-faster%2dcpython-dry_freelists-3.12.0a0-d09385f |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 127 ms: 1.07x faster                                                     |
| regex_effbot   | 3.46 ms                                                | 3.43 ms: 1.01x faster                                                    |
| regex_v8       | 22.2 ms                                                | 22.3 ms: 1.00x slower                                                    |
| regex_dna      | 203 ms                                                 | 218 ms: 1.07x slower                                                     |
| Geometric mean | (ref)                                                  | 1.00x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221014-linux-x86_64-faster%2dcpython-dry_freelists-3.12.0a0-d09385f |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.30 ms: 1.33x faster                                                    |
| unpickle_pure_python | 227 us                                                 | 203 us: 1.12x faster                                                     |
| json_loads           | 26.1 us                                                | 23.4 us: 1.11x faster                                                    |
| pickle_pure_python   | 308 us                                                 | 287 us: 1.07x faster                                                     |
| xml_etree_iterparse  | 104 ms                                                 | 102 ms: 1.02x faster                                                     |
| xml_etree_parse      | 160 ms                                                 | 158 ms: 1.02x faster                                                     |
| pickle_list          | 4.14 us                                                | 4.10 us: 1.01x faster                                                    |
| xml_etree_generate   | 75.9 ms                                                | 75.6 ms: 1.00x faster                                                    |
| xml_etree_process    | 53.7 ms                                                | 53.9 ms: 1.00x slower                                                    |
| pickle               | 9.90 us                                                | 10.3 us: 1.04x slower                                                    |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                             |

Benchmark hidden because not significant (3): unpickle, unpickle_list, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221014-linux-x86_64-faster%2dcpython-dry_freelists-3.12.0a0-d09385f |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.41 ms: 1.02x faster                                                    |
| python_startup_no_site | 6.04 ms                                                | 5.94 ms: 1.02x faster                                                    |
| Geometric mean         | (ref)                                                  | 1.02x faster                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221014-linux-x86_64-faster%2dcpython-dry_freelists-3.12.0a0-d09385f |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_xml      | 51.4 ms                                                | 49.1 ms: 1.05x faster                                                    |
| genshi_text     | 21.5 ms                                                | 20.8 ms: 1.04x faster                                                    |
| django_template | 32.3 ms                                                | 32.5 ms: 1.01x slower                                                    |
| mako            | 9.83 ms                                                | 9.89 ms: 1.01x slower                                                    |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                             |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221014-linux-x86_64-faster%2dcpython-dry_freelists-3.12.0a0-d09385f |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| json_dumps              | 12.4 ms                                                | 9.30 ms: 1.33x faster                                                    |
| scimark_sparse_mat_mult | 4.59 ms                                                | 4.05 ms: 1.13x faster                                                    |
| deltablue               | 3.66 ms                                                | 3.27 ms: 1.12x faster                                                    |
| unpickle_pure_python    | 227 us                                                 | 203 us: 1.12x faster                                                     |
| json_loads              | 26.1 us                                                | 23.4 us: 1.11x faster                                                    |
| richards                | 46.1 ms                                                | 42.3 ms: 1.09x faster                                                    |
| json                    | 4.87 ms                                                | 4.48 ms: 1.09x faster                                                    |
| html5lib                | 64.8 ms                                                | 59.6 ms: 1.09x faster                                                    |
| sqlalchemy_imperative   | 18.1 ms                                                | 16.7 ms: 1.08x faster                                                    |
| pickle_pure_python      | 308 us                                                 | 287 us: 1.07x faster                                                     |
| regex_compile           | 136 ms                                                 | 127 ms: 1.07x faster                                                     |
| go                      | 140 ms                                                 | 131 ms: 1.07x faster                                                     |
| coroutines              | 26.2 ms                                                | 24.5 ms: 1.07x faster                                                    |
| scimark_sor             | 115 ms                                                 | 108 ms: 1.07x faster                                                     |
| pycparser               | 1.19 sec                                               | 1.11 sec: 1.07x faster                                                   |
| float                   | 76.8 ms                                                | 72.1 ms: 1.06x faster                                                    |
| nqueens                 | 83.8 ms                                                | 78.9 ms: 1.06x faster                                                    |
| logging_silent          | 98.0 ns                                                | 92.5 ns: 1.06x faster                                                    |
| aiohttp                 | 1.05 ms                                                | 991 us: 1.06x faster                                                     |
| pprint_pformat          | 1.46 sec                                               | 1.38 sec: 1.06x faster                                                   |
| pprint_safe_repr        | 706 ms                                                 | 670 ms: 1.05x faster                                                     |
| sympy_expand            | 475 ms                                                 | 453 ms: 1.05x faster                                                     |
| fannkuch                | 384 ms                                                 | 366 ms: 1.05x faster                                                     |
| create_gc_cycles        | 1.52 ms                                                | 1.44 ms: 1.05x faster                                                    |
| genshi_xml              | 51.4 ms                                                | 49.1 ms: 1.05x faster                                                    |
| pyflate                 | 419 ms                                                 | 400 ms: 1.05x faster                                                     |
| logging_simple          | 6.02 us                                                | 5.76 us: 1.05x faster                                                    |
| bench_thread_pool       | 817 us                                                 | 782 us: 1.04x faster                                                     |
| 2to3                    | 259 ms                                                 | 248 ms: 1.04x faster                                                     |
| gunicorn                | 1.12 ms                                                | 1.07 ms: 1.04x faster                                                    |
| hexiom                  | 6.34 ms                                                | 6.08 ms: 1.04x faster                                                    |
| sqlalchemy_declarative  | 138 ms                                                 | 133 ms: 1.04x faster                                                     |
| sympy_str               | 291 ms                                                 | 280 ms: 1.04x faster                                                     |
| tornado_http            | 96.5 ms                                                | 92.8 ms: 1.04x faster                                                    |
| docutils                | 2.60 sec                                               | 2.50 sec: 1.04x faster                                                   |
| chaos                   | 68.7 ms                                                | 66.2 ms: 1.04x faster                                                    |
| genshi_text             | 21.5 ms                                                | 20.8 ms: 1.04x faster                                                    |
| deepcopy                | 341 us                                                 | 330 us: 1.03x faster                                                     |
| scimark_fft             | 325 ms                                                 | 315 ms: 1.03x faster                                                     |
| deepcopy_reduce         | 3.02 us                                                | 2.92 us: 1.03x faster                                                    |
| sympy_integrate         | 21.0 ms                                                | 20.3 ms: 1.03x faster                                                    |
| scimark_monte_carlo     | 68.0 ms                                                | 65.9 ms: 1.03x faster                                                    |
| deepcopy_memo           | 35.8 us                                                | 34.7 us: 1.03x faster                                                    |
| async_tree_none         | 526 ms                                                 | 514 ms: 1.02x faster                                                     |
| thrift                  | 760 us                                                 | 742 us: 1.02x faster                                                     |
| sqlglot_optimize        | 52.7 ms                                                | 51.5 ms: 1.02x faster                                                    |
| sqlglot_normalize       | 108 ms                                                 | 105 ms: 1.02x faster                                                     |
| xml_etree_iterparse     | 104 ms                                                 | 102 ms: 1.02x faster                                                     |
| sympy_sum               | 166 ms                                                 | 162 ms: 1.02x faster                                                     |
| python_startup          | 8.58 ms                                                | 8.41 ms: 1.02x faster                                                    |
| async_generators        | 356 ms                                                 | 349 ms: 1.02x faster                                                     |
| dulwich_log             | 64.0 ms                                                | 62.8 ms: 1.02x faster                                                    |
| python_startup_no_site  | 6.04 ms                                                | 5.94 ms: 1.02x faster                                                    |
| xml_etree_parse         | 160 ms                                                 | 158 ms: 1.02x faster                                                     |
| logging_format          | 6.48 us                                                | 6.37 us: 1.02x faster                                                    |
| async_tree_cpu_io_mixed | 736 ms                                                 | 724 ms: 1.02x faster                                                     |
| sqlglot_parse           | 1.36 ms                                                | 1.34 ms: 1.01x faster                                                    |
| mdp                     | 2.63 sec                                               | 2.59 sec: 1.01x faster                                                   |
| asyncio_tcp             | 883 ms                                                 | 872 ms: 1.01x faster                                                     |
| pathlib                 | 18.1 ms                                                | 17.8 ms: 1.01x faster                                                    |
| unpack_sequence         | 44.5 ns                                                | 44.0 ns: 1.01x faster                                                    |
| coverage                | 99.3 ms                                                | 98.3 ms: 1.01x faster                                                    |
| sqlglot_transpile       | 1.65 ms                                                | 1.63 ms: 1.01x faster                                                    |
| pickle_list             | 4.14 us                                                | 4.10 us: 1.01x faster                                                    |
| regex_effbot            | 3.46 ms                                                | 3.43 ms: 1.01x faster                                                    |
| xml_etree_generate      | 75.9 ms                                                | 75.6 ms: 1.00x faster                                                    |
| regex_v8                | 22.2 ms                                                | 22.3 ms: 1.00x slower                                                    |
| xml_etree_process       | 53.7 ms                                                | 53.9 ms: 1.00x slower                                                    |
| django_template         | 32.3 ms                                                | 32.5 ms: 1.01x slower                                                    |
| mako                    | 9.83 ms                                                | 9.89 ms: 1.01x slower                                                    |
| async_tree_io           | 1.30 sec                                               | 1.31 sec: 1.01x slower                                                   |
| chameleon               | 6.38 ms                                                | 6.46 ms: 1.01x slower                                                    |
| scimark_lu              | 108 ms                                                 | 110 ms: 1.02x slower                                                     |
| async_tree_memoization  | 624 ms                                                 | 636 ms: 1.02x slower                                                     |
| telco                   | 6.43 ms                                                | 6.58 ms: 1.02x slower                                                    |
| generators              | 73.5 ms                                                | 75.4 ms: 1.03x slower                                                    |
| sqlite_synth            | 2.48 us                                                | 2.56 us: 1.03x slower                                                    |
| pickle                  | 9.90 us                                                | 10.3 us: 1.04x slower                                                    |
| spectral_norm           | 98.1 ms                                                | 102 ms: 1.04x slower                                                     |
| pidigits                | 197 ms                                                 | 206 ms: 1.05x slower                                                     |
| gc_traversal            | 3.82 ms                                                | 4.03 ms: 1.06x slower                                                    |
| nbody                   | 90.0 ms                                                | 95.2 ms: 1.06x slower                                                    |
| regex_dna               | 203 ms                                                 | 218 ms: 1.07x slower                                                     |
| dask                    | 365 ms                                                 | 496 ms: 1.36x slower                                                     |
| Geometric mean          | (ref)                                                  | 1.03x faster                                                             |

Benchmark hidden because not significant (9): pylint, unpickle, raytrace, unpickle_list, pickle_dict, bench_mp_pool, djangocms, crypto_pyaes, meteor_contest
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, mypy2
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20221014-3.12.0a0-d09385f/bm-20221014-linux-x86_64-faster%2dcpython-dry_freelists-3.12.0a0-d09385f.json: mypy
