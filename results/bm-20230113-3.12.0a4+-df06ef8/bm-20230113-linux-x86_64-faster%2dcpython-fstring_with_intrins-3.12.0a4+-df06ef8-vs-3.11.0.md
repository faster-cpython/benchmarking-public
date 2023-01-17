
# Results vs. 3.11.0

- fork: faster-cpython
- ref: fstring_with_intrins
- machine: linux-x86_64
- commit hash: df06ef8
- commit date: 2023-01-13
- overall geometric mean: 1.03x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230113-linux-x86_64-faster%2dcpython-fstring_with_intrins-3.12.0a4+-df06ef8 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 257 ms                                                 | 253 ms: 1.02x faster                                                             |
| chameleon      | 6.41 ms                                                | 6.37 ms: 1.01x faster                                                            |
| docutils       | 2.60 sec                                               | 2.51 sec: 1.03x faster                                                           |
| html5lib       | 63.2 ms                                                | 60.2 ms: 1.05x faster                                                            |
| tornado_http   | 96.6 ms                                                | 93.4 ms: 1.03x faster                                                            |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230113-linux-x86_64-faster%2dcpython-fstring_with_intrins-3.12.0a4+-df06ef8 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| float          | 76.3 ms                                                | 72.2 ms: 1.06x faster                                                            |
| nbody          | 95.0 ms                                                | 93.7 ms: 1.01x faster                                                            |
| pidigits       | 199 ms                                                 | 189 ms: 1.05x faster                                                             |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230113-linux-x86_64-faster%2dcpython-fstring_with_intrins-3.12.0a4+-df06ef8 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 130 ms: 1.04x faster                                                             |
| regex_dna      | 203 ms                                                 | 210 ms: 1.03x slower                                                             |
| regex_effbot   | 3.36 ms                                                | 3.58 ms: 1.07x slower                                                            |
| regex_v8       | 22.3 ms                                                | 21.8 ms: 1.02x faster                                                            |
| Geometric mean | (ref)                                                  | 1.01x slower                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230113-linux-x86_64-faster%2dcpython-fstring_with_intrins-3.12.0a4+-df06ef8 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| json_dumps           | 12.7 ms                                                | 9.46 ms: 1.34x faster                                                            |
| json_loads           | 26.2 us                                                | 24.0 us: 1.09x faster                                                            |
| pickle               | 9.79 us                                                | 10.1 us: 1.03x slower                                                            |
| pickle_dict          | 31.4 us                                                | 30.7 us: 1.02x faster                                                            |
| pickle_list          | 4.17 us                                                | 4.10 us: 1.02x faster                                                            |
| pickle_pure_python   | 304 us                                                 | 283 us: 1.08x faster                                                             |
| unpickle_pure_python | 225 us                                                 | 198 us: 1.14x faster                                                             |
| xml_etree_parse      | 158 ms                                                 | 149 ms: 1.06x faster                                                             |
| xml_etree_iterparse  | 103 ms                                                 | 105 ms: 1.03x slower                                                             |
| xml_etree_generate   | 76.2 ms                                                | 77.5 ms: 1.02x slower                                                            |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                                     |

Benchmark hidden because not significant (3): unpickle, unpickle_list, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230113-linux-x86_64-faster%2dcpython-fstring_with_intrins-3.12.0a4+-df06ef8 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 8.36 ms                                                | 8.57 ms: 1.03x slower                                                            |
| python_startup_no_site | 5.96 ms                                                | 6.13 ms: 1.03x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.03x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230113-linux-x86_64-faster%2dcpython-fstring_with_intrins-3.12.0a4+-df06ef8 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| django_template | 32.5 ms                                                | 32.2 ms: 1.01x faster                                                            |
| genshi_text     | 22.1 ms                                                | 20.5 ms: 1.08x faster                                                            |
| genshi_xml      | 52.1 ms                                                | 46.5 ms: 1.12x faster                                                            |
| mako            | 9.85 ms                                                | 9.75 ms: 1.01x faster                                                            |
| Geometric mean  | (ref)                                                  | 1.05x faster                                                                     |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230113-linux-x86_64-faster%2dcpython-fstring_with_intrins-3.12.0a4+-df06ef8 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3                    | 257 ms                                                 | 253 ms: 1.02x faster                                                             |
| aiohttp                 | 1.05 ms                                                | 1.00 ms: 1.05x faster                                                            |
| async_generators        | 359 ms                                                 | 355 ms: 1.01x faster                                                             |
| async_tree_none         | 529 ms                                                 | 523 ms: 1.01x faster                                                             |
| async_tree_io           | 1.31 sec                                               | 1.33 sec: 1.02x slower                                                           |
| async_tree_memoization  | 625 ms                                                 | 656 ms: 1.05x slower                                                             |
| chameleon               | 6.41 ms                                                | 6.37 ms: 1.01x faster                                                            |
| chaos                   | 68.6 ms                                                | 66.9 ms: 1.03x faster                                                            |
| bench_thread_pool       | 810 us                                                 | 778 us: 1.04x faster                                                             |
| coroutines              | 26.1 ms                                                | 24.7 ms: 1.06x faster                                                            |
| coverage                | 101 ms                                                 | 99.6 ms: 1.01x faster                                                            |
| crypto_pyaes            | 73.9 ms                                                | 74.3 ms: 1.01x slower                                                            |
| deepcopy                | 344 us                                                 | 332 us: 1.04x faster                                                             |
| deepcopy_reduce         | 2.97 us                                                | 2.89 us: 1.03x faster                                                            |
| deepcopy_memo           | 36.4 us                                                | 33.5 us: 1.09x faster                                                            |
| deltablue               | 3.64 ms                                                | 3.19 ms: 1.14x faster                                                            |
| django_template         | 32.5 ms                                                | 32.2 ms: 1.01x faster                                                            |
| docutils                | 2.60 sec                                               | 2.51 sec: 1.03x faster                                                           |
| dulwich_log             | 63.9 ms                                                | 61.6 ms: 1.04x faster                                                            |
| fannkuch                | 388 ms                                                 | 366 ms: 1.06x faster                                                             |
| float                   | 76.3 ms                                                | 72.2 ms: 1.06x faster                                                            |
| generators              | 72.2 ms                                                | 77.2 ms: 1.07x slower                                                            |
| genshi_text             | 22.1 ms                                                | 20.5 ms: 1.08x faster                                                            |
| genshi_xml              | 52.1 ms                                                | 46.5 ms: 1.12x faster                                                            |
| go                      | 143 ms                                                 | 134 ms: 1.07x faster                                                             |
| gunicorn                | 1.12 ms                                                | 1.07 ms: 1.05x faster                                                            |
| hexiom                  | 6.35 ms                                                | 5.95 ms: 1.07x faster                                                            |
| html5lib                | 63.2 ms                                                | 60.2 ms: 1.05x faster                                                            |
| json                    | 4.95 ms                                                | 4.72 ms: 1.05x faster                                                            |
| json_dumps              | 12.7 ms                                                | 9.46 ms: 1.34x faster                                                            |
| json_loads              | 26.2 us                                                | 24.0 us: 1.09x faster                                                            |
| logging_format          | 6.62 us                                                | 6.31 us: 1.05x faster                                                            |
| logging_silent          | 98.5 ns                                                | 91.5 ns: 1.08x faster                                                            |
| logging_simple          | 6.06 us                                                | 5.71 us: 1.06x faster                                                            |
| mako                    | 9.85 ms                                                | 9.75 ms: 1.01x faster                                                            |
| mdp                     | 2.62 sec                                               | 2.47 sec: 1.06x faster                                                           |
| meteor_contest          | 105 ms                                                 | 104 ms: 1.01x faster                                                             |
| mypy                    | 669 ms                                                 | 810 ms: 1.21x slower                                                             |
| nbody                   | 95.0 ms                                                | 93.7 ms: 1.01x faster                                                            |
| nqueens                 | 85.0 ms                                                | 79.4 ms: 1.07x faster                                                            |
| pathlib                 | 18.2 ms                                                | 17.9 ms: 1.02x faster                                                            |
| pickle                  | 9.79 us                                                | 10.1 us: 1.03x slower                                                            |
| pickle_dict             | 31.4 us                                                | 30.7 us: 1.02x faster                                                            |
| pickle_list             | 4.17 us                                                | 4.10 us: 1.02x faster                                                            |
| pickle_pure_python      | 304 us                                                 | 283 us: 1.08x faster                                                             |
| pidigits                | 199 ms                                                 | 189 ms: 1.05x faster                                                             |
| pprint_safe_repr        | 691 ms                                                 | 666 ms: 1.04x faster                                                             |
| pprint_pformat          | 1.44 sec                                               | 1.37 sec: 1.06x faster                                                           |
| pycparser               | 1.17 sec                                               | 1.09 sec: 1.08x faster                                                           |
| pyflate                 | 417 ms                                                 | 394 ms: 1.06x faster                                                             |
| python_startup          | 8.36 ms                                                | 8.57 ms: 1.03x slower                                                            |
| python_startup_no_site  | 5.96 ms                                                | 6.13 ms: 1.03x slower                                                            |
| raytrace                | 290 ms                                                 | 287 ms: 1.01x faster                                                             |
| regex_compile           | 136 ms                                                 | 130 ms: 1.04x faster                                                             |
| regex_dna               | 203 ms                                                 | 210 ms: 1.03x slower                                                             |
| regex_effbot            | 3.36 ms                                                | 3.58 ms: 1.07x slower                                                            |
| regex_v8                | 22.3 ms                                                | 21.8 ms: 1.02x faster                                                            |
| richards                | 46.2 ms                                                | 42.3 ms: 1.09x faster                                                            |
| scimark_fft             | 329 ms                                                 | 312 ms: 1.05x faster                                                             |
| scimark_monte_carlo     | 68.3 ms                                                | 64.3 ms: 1.06x faster                                                            |
| scimark_sor             | 115 ms                                                 | 107 ms: 1.08x faster                                                             |
| scimark_sparse_mat_mult | 4.40 ms                                                | 4.01 ms: 1.10x faster                                                            |
| spectral_norm           | 99.9 ms                                                | 97.6 ms: 1.02x faster                                                            |
| sqlglot_parse           | 1.37 ms                                                | 1.40 ms: 1.02x slower                                                            |
| sqlglot_transpile       | 1.66 ms                                                | 1.69 ms: 1.02x slower                                                            |
| sqlglot_optimize        | 53.0 ms                                                | 51.0 ms: 1.04x faster                                                            |
| sqlglot_normalize       | 108 ms                                                 | 105 ms: 1.03x faster                                                             |
| sqlite_synth            | 2.49 us                                                | 2.56 us: 1.03x slower                                                            |
| sympy_expand            | 472 ms                                                 | 457 ms: 1.03x faster                                                             |
| sympy_integrate         | 20.9 ms                                                | 20.3 ms: 1.03x faster                                                            |
| sympy_sum               | 166 ms                                                 | 164 ms: 1.01x faster                                                             |
| sympy_str               | 287 ms                                                 | 281 ms: 1.02x faster                                                             |
| telco                   | 6.62 ms                                                | 6.24 ms: 1.06x faster                                                            |
| thrift                  | 752 us                                                 | 746 us: 1.01x faster                                                             |
| tornado_http            | 96.6 ms                                                | 93.4 ms: 1.03x faster                                                            |
| unpack_sequence         | 43.4 ns                                                | 43.0 ns: 1.01x faster                                                            |
| unpickle_pure_python    | 225 us                                                 | 198 us: 1.14x faster                                                             |
| xml_etree_parse         | 158 ms                                                 | 149 ms: 1.06x faster                                                             |
| xml_etree_iterparse     | 103 ms                                                 | 105 ms: 1.03x slower                                                             |
| xml_etree_generate      | 76.2 ms                                                | 77.5 ms: 1.02x slower                                                            |
| Geometric mean          | (ref)                                                  | 1.03x faster                                                                     |

Benchmark hidden because not significant (6): async_tree_cpu_io_mixed, bench_mp_pool, scimark_lu, unpickle, unpickle_list, xml_etree_process
Ignored benchmarks (4) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20230113-3.12.0a4+-df06ef8/bm-20230113-linux-x86_64-faster%2dcpython-fstring_with_intrins-3.12.0a4+-df06ef8.json: asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal
