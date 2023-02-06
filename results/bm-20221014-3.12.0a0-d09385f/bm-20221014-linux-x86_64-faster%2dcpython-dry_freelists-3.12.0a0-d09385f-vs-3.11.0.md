
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
| 2to3           | 257 ms                                                 | 246 ms: 1.05x faster                                                     |
| chameleon      | 6.41 ms                                                | 6.46 ms: 1.01x slower                                                    |
| docutils       | 2.60 sec                                               | 2.51 sec: 1.03x faster                                                   |
| html5lib       | 63.2 ms                                                | 59.8 ms: 1.06x faster                                                    |
| tornado_http   | 96.6 ms                                                | 93.2 ms: 1.04x faster                                                    |
| Geometric mean | (ref)                                                  | 1.03x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221014-linux-x86_64-faster%2dcpython-dry_freelists-3.12.0a0-d09385f |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 76.3 ms                                                | 71.8 ms: 1.06x faster                                                    |
| pidigits       | 199 ms                                                 | 191 ms: 1.05x faster                                                     |
| Geometric mean | (ref)                                                  | 1.04x faster                                                             |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221014-linux-x86_64-faster%2dcpython-dry_freelists-3.12.0a0-d09385f |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 129 ms: 1.06x faster                                                     |
| regex_v8       | 22.3 ms                                                | 21.8 ms: 1.02x faster                                                    |
| regex_dna      | 203 ms                                                 | 206 ms: 1.01x slower                                                     |
| regex_effbot   | 3.36 ms                                                | 3.63 ms: 1.08x slower                                                    |
| Geometric mean | (ref)                                                  | 1.00x slower                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221014-linux-x86_64-faster%2dcpython-dry_freelists-3.12.0a0-d09385f |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| json_dumps           | 12.7 ms                                                | 9.42 ms: 1.34x faster                                                    |
| json_loads           | 26.2 us                                                | 23.5 us: 1.12x faster                                                    |
| unpickle_pure_python | 225 us                                                 | 203 us: 1.11x faster                                                     |
| pickle_list          | 4.17 us                                                | 3.95 us: 1.06x faster                                                    |
| pickle_dict          | 31.4 us                                                | 30.0 us: 1.05x faster                                                    |
| pickle_pure_python   | 304 us                                                 | 291 us: 1.05x faster                                                     |
| unpickle_list        | 4.95 us                                                | 4.88 us: 1.01x faster                                                    |
| pickle               | 9.79 us                                                | 10.1 us: 1.03x slower                                                    |
| xml_etree_iterparse  | 103 ms                                                 | 106 ms: 1.03x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                             |

Benchmark hidden because not significant (4): unpickle, xml_etree_generate, xml_etree_process, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221014-linux-x86_64-faster%2dcpython-dry_freelists-3.12.0a0-d09385f |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 5.96 ms                                                | 5.95 ms: 1.00x faster                                                    |
| python_startup         | 8.36 ms                                                | 8.43 ms: 1.01x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.00x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221014-linux-x86_64-faster%2dcpython-dry_freelists-3.12.0a0-d09385f |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_xml      | 52.1 ms                                                | 48.6 ms: 1.07x faster                                                    |
| genshi_text     | 22.1 ms                                                | 20.7 ms: 1.07x faster                                                    |
| mako            | 9.85 ms                                                | 9.60 ms: 1.03x faster                                                    |
| django_template | 32.5 ms                                                | 32.2 ms: 1.01x faster                                                    |
| Geometric mean  | (ref)                                                  | 1.04x faster                                                             |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221014-linux-x86_64-faster%2dcpython-dry_freelists-3.12.0a0-d09385f |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| json_dumps              | 12.7 ms                                                | 9.42 ms: 1.34x faster                                                    |
| json_loads              | 26.2 us                                                | 23.5 us: 1.12x faster                                                    |
| unpickle_pure_python    | 225 us                                                 | 203 us: 1.11x faster                                                     |
| deltablue               | 3.64 ms                                                | 3.29 ms: 1.11x faster                                                    |
| json                    | 4.95 ms                                                | 4.48 ms: 1.10x faster                                                    |
| go                      | 143 ms                                                 | 132 ms: 1.09x faster                                                     |
| nqueens                 | 85.0 ms                                                | 78.5 ms: 1.08x faster                                                    |
| richards                | 46.2 ms                                                | 42.8 ms: 1.08x faster                                                    |
| genshi_xml              | 52.1 ms                                                | 48.6 ms: 1.07x faster                                                    |
| logging_silent          | 98.5 ns                                                | 91.9 ns: 1.07x faster                                                    |
| scimark_sor             | 115 ms                                                 | 107 ms: 1.07x faster                                                     |
| logging_simple          | 6.06 us                                                | 5.67 us: 1.07x faster                                                    |
| genshi_text             | 22.1 ms                                                | 20.7 ms: 1.07x faster                                                    |
| fannkuch                | 388 ms                                                 | 365 ms: 1.06x faster                                                     |
| float                   | 76.3 ms                                                | 71.8 ms: 1.06x faster                                                    |
| sqlalchemy_imperative   | 18.0 ms                                                | 17.0 ms: 1.06x faster                                                    |
| deepcopy_memo           | 36.4 us                                                | 34.4 us: 1.06x faster                                                    |
| pickle_list             | 4.17 us                                                | 3.95 us: 1.06x faster                                                    |
| pycparser               | 1.17 sec                                               | 1.11 sec: 1.06x faster                                                   |
| regex_compile           | 136 ms                                                 | 129 ms: 1.06x faster                                                     |
| pprint_pformat          | 1.44 sec                                               | 1.37 sec: 1.06x faster                                                   |
| html5lib                | 63.2 ms                                                | 59.8 ms: 1.06x faster                                                    |
| aiohttp                 | 1.05 ms                                                | 993 us: 1.05x faster                                                     |
| pyflate                 | 417 ms                                                 | 397 ms: 1.05x faster                                                     |
| pickle_dict             | 31.4 us                                                | 30.0 us: 1.05x faster                                                    |
| gunicorn                | 1.12 ms                                                | 1.07 ms: 1.05x faster                                                    |
| pidigits                | 199 ms                                                 | 191 ms: 1.05x faster                                                     |
| 2to3                    | 257 ms                                                 | 246 ms: 1.05x faster                                                     |
| pickle_pure_python      | 304 us                                                 | 291 us: 1.05x faster                                                     |
| mypy                    | 669 ms                                                 | 640 ms: 1.04x faster                                                     |
| logging_format          | 6.62 us                                                | 6.34 us: 1.04x faster                                                    |
| sympy_expand            | 472 ms                                                 | 453 ms: 1.04x faster                                                     |
| scimark_sparse_mat_mult | 4.40 ms                                                | 4.22 ms: 1.04x faster                                                    |
| sqlalchemy_declarative  | 139 ms                                                 | 134 ms: 1.04x faster                                                     |
| tornado_http            | 96.6 ms                                                | 93.2 ms: 1.04x faster                                                    |
| docutils                | 2.60 sec                                               | 2.51 sec: 1.03x faster                                                   |
| bench_thread_pool       | 810 us                                                 | 783 us: 1.03x faster                                                     |
| telco                   | 6.62 ms                                                | 6.41 ms: 1.03x faster                                                    |
| scimark_monte_carlo     | 68.3 ms                                                | 66.1 ms: 1.03x faster                                                    |
| scimark_fft             | 329 ms                                                 | 320 ms: 1.03x faster                                                     |
| raytrace                | 290 ms                                                 | 282 ms: 1.03x faster                                                     |
| sqlglot_optimize        | 53.0 ms                                                | 51.6 ms: 1.03x faster                                                    |
| sqlglot_normalize       | 108 ms                                                 | 105 ms: 1.03x faster                                                     |
| hexiom                  | 6.35 ms                                                | 6.18 ms: 1.03x faster                                                    |
| deepcopy_reduce         | 2.97 us                                                | 2.89 us: 1.03x faster                                                    |
| mako                    | 9.85 ms                                                | 9.60 ms: 1.03x faster                                                    |
| pprint_safe_repr        | 691 ms                                                 | 674 ms: 1.02x faster                                                     |
| deepcopy                | 344 us                                                 | 336 us: 1.02x faster                                                     |
| async_tree_cpu_io_mixed | 752 ms                                                 | 734 ms: 1.02x faster                                                     |
| async_tree_none         | 529 ms                                                 | 517 ms: 1.02x faster                                                     |
| regex_v8                | 22.3 ms                                                | 21.8 ms: 1.02x faster                                                    |
| sympy_integrate         | 20.9 ms                                                | 20.4 ms: 1.02x faster                                                    |
| dulwich_log             | 63.9 ms                                                | 62.5 ms: 1.02x faster                                                    |
| sympy_str               | 287 ms                                                 | 282 ms: 1.02x faster                                                     |
| sympy_sum               | 166 ms                                                 | 163 ms: 1.02x faster                                                     |
| sqlglot_parse           | 1.37 ms                                                | 1.34 ms: 1.02x faster                                                    |
| coverage                | 101 ms                                                 | 98.9 ms: 1.02x faster                                                    |
| coroutines              | 26.1 ms                                                | 25.7 ms: 1.02x faster                                                    |
| unpickle_list           | 4.95 us                                                | 4.88 us: 1.01x faster                                                    |
| sqlglot_transpile       | 1.66 ms                                                | 1.64 ms: 1.01x faster                                                    |
| async_generators        | 359 ms                                                 | 355 ms: 1.01x faster                                                     |
| chaos                   | 68.6 ms                                                | 67.9 ms: 1.01x faster                                                    |
| spectral_norm           | 99.9 ms                                                | 99.0 ms: 1.01x faster                                                    |
| meteor_contest          | 105 ms                                                 | 104 ms: 1.01x faster                                                     |
| thrift                  | 752 us                                                 | 746 us: 1.01x faster                                                     |
| django_template         | 32.5 ms                                                | 32.2 ms: 1.01x faster                                                    |
| python_startup_no_site  | 5.96 ms                                                | 5.95 ms: 1.00x faster                                                    |
| chameleon               | 6.41 ms                                                | 6.46 ms: 1.01x slower                                                    |
| python_startup          | 8.36 ms                                                | 8.43 ms: 1.01x slower                                                    |
| unpack_sequence         | 43.4 ns                                                | 43.8 ns: 1.01x slower                                                    |
| regex_dna               | 203 ms                                                 | 206 ms: 1.01x slower                                                     |
| async_tree_memoization  | 625 ms                                                 | 633 ms: 1.01x slower                                                     |
| generators              | 72.2 ms                                                | 73.3 ms: 1.02x slower                                                    |
| crypto_pyaes            | 73.9 ms                                                | 76.3 ms: 1.03x slower                                                    |
| pickle                  | 9.79 us                                                | 10.1 us: 1.03x slower                                                    |
| xml_etree_iterparse     | 103 ms                                                 | 106 ms: 1.03x slower                                                     |
| sqlite_synth            | 2.49 us                                                | 2.58 us: 1.03x slower                                                    |
| mdp                     | 2.62 sec                                               | 2.71 sec: 1.03x slower                                                   |
| scimark_lu              | 107 ms                                                 | 113 ms: 1.05x slower                                                     |
| regex_effbot            | 3.36 ms                                                | 3.63 ms: 1.08x slower                                                    |
| Geometric mean          | (ref)                                                  | 1.03x faster                                                             |

Benchmark hidden because not significant (9): unpickle, pylint, nbody, pathlib, bench_mp_pool, xml_etree_generate, xml_etree_process, async_tree_io, xml_etree_parse
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20221014-3.12.0a0-d09385f/bm-20221014-linux-x86_64-faster%2dcpython-dry_freelists-3.12.0a0-d09385f.json: asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal
