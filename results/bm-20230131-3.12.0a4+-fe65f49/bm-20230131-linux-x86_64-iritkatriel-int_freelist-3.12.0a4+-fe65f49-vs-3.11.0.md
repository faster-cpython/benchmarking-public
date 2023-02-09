
# Results vs. 3.11.0

- fork: iritkatriel
- ref: int_freelist
- machine: linux-x86_64
- commit hash: fe65f49
- commit date: 2023-01-31
- overall geometric mean: 1.01x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-fe65f49 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 257 ms                                                 | 253 ms: 1.02x faster                                                |
| chameleon      | 6.41 ms                                                | 6.29 ms: 1.02x faster                                               |
| docutils       | 2.60 sec                                               | 2.51 sec: 1.03x faster                                              |
| html5lib       | 63.2 ms                                                | 61.9 ms: 1.02x faster                                               |
| tornado_http   | 96.6 ms                                                | 95.0 ms: 1.02x faster                                               |
| Geometric mean | (ref)                                                  | 1.02x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-fe65f49 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 76.3 ms                                                | 72.8 ms: 1.05x faster                                               |
| pidigits       | 199 ms                                                 | 192 ms: 1.04x faster                                                |
| nbody          | 95.0 ms                                                | 97.9 ms: 1.03x slower                                               |
| Geometric mean | (ref)                                                  | 1.02x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-fe65f49 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 128 ms: 1.06x faster                                                |
| regex_v8       | 22.3 ms                                                | 21.7 ms: 1.03x faster                                               |
| regex_dna      | 203 ms                                                 | 210 ms: 1.03x slower                                                |
| regex_effbot   | 3.36 ms                                                | 3.50 ms: 1.04x slower                                               |
| Geometric mean | (ref)                                                  | 1.00x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-fe65f49 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| json_dumps           | 12.7 ms                                                | 9.35 ms: 1.35x faster                                               |
| unpickle_pure_python | 225 us                                                 | 199 us: 1.13x faster                                                |
| json_loads           | 26.2 us                                                | 24.6 us: 1.07x faster                                               |
| xml_etree_parse      | 158 ms                                                 | 148 ms: 1.07x faster                                                |
| pickle_pure_python   | 304 us                                                 | 285 us: 1.06x faster                                                |
| pickle_dict          | 31.4 us                                                | 30.5 us: 1.03x faster                                               |
| pickle_list          | 4.17 us                                                | 4.09 us: 1.02x faster                                               |
| unpickle_list        | 4.95 us                                                | 4.90 us: 1.01x faster                                               |
| xml_etree_process    | 53.8 ms                                                | 53.2 ms: 1.01x faster                                               |
| xml_etree_iterparse  | 103 ms                                                 | 102 ms: 1.01x faster                                                |
| xml_etree_generate   | 76.2 ms                                                | 77.7 ms: 1.02x slower                                               |
| unpickle             | 13.3 us                                                | 13.6 us: 1.02x slower                                               |
| pickle               | 9.79 us                                                | 10.3 us: 1.05x slower                                               |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-fe65f49 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 8.36 ms                                                | 8.94 ms: 1.07x slower                                               |
| python_startup_no_site | 5.96 ms                                                | 6.47 ms: 1.08x slower                                               |
| Geometric mean         | (ref)                                                  | 1.08x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-fe65f49 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_xml      | 52.1 ms                                                | 47.0 ms: 1.11x faster                                               |
| genshi_text     | 22.1 ms                                                | 20.2 ms: 1.09x faster                                               |
| mako            | 9.85 ms                                                | 9.82 ms: 1.00x faster                                               |
| django_template | 32.5 ms                                                | 32.6 ms: 1.01x slower                                               |
| Geometric mean  | (ref)                                                  | 1.05x faster                                                        |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-fe65f49 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| json_dumps              | 12.7 ms                                                | 9.35 ms: 1.35x faster                                               |
| unpickle_pure_python    | 225 us                                                 | 199 us: 1.13x faster                                                |
| deltablue               | 3.64 ms                                                | 3.24 ms: 1.12x faster                                               |
| genshi_xml              | 52.1 ms                                                | 47.0 ms: 1.11x faster                                               |
| genshi_text             | 22.1 ms                                                | 20.2 ms: 1.09x faster                                               |
| logging_silent          | 98.5 ns                                                | 91.3 ns: 1.08x faster                                               |
| nqueens                 | 85.0 ms                                                | 79.3 ms: 1.07x faster                                               |
| sympy_sum               | 166 ms                                                 | 155 ms: 1.07x faster                                                |
| json_loads              | 26.2 us                                                | 24.6 us: 1.07x faster                                               |
| xml_etree_parse         | 158 ms                                                 | 148 ms: 1.07x faster                                                |
| pickle_pure_python      | 304 us                                                 | 285 us: 1.06x faster                                                |
| sympy_str               | 287 ms                                                 | 270 ms: 1.06x faster                                                |
| regex_compile           | 136 ms                                                 | 128 ms: 1.06x faster                                                |
| logging_simple          | 6.06 us                                                | 5.72 us: 1.06x faster                                               |
| hexiom                  | 6.35 ms                                                | 5.99 ms: 1.06x faster                                               |
| json                    | 4.95 ms                                                | 4.67 ms: 1.06x faster                                               |
| coverage                | 101 ms                                                 | 95.1 ms: 1.06x faster                                               |
| richards                | 46.2 ms                                                | 43.8 ms: 1.05x faster                                               |
| sympy_integrate         | 20.9 ms                                                | 19.8 ms: 1.05x faster                                               |
| logging_format          | 6.62 us                                                | 6.29 us: 1.05x faster                                               |
| fannkuch                | 388 ms                                                 | 369 ms: 1.05x faster                                                |
| deepcopy_memo           | 36.4 us                                                | 34.7 us: 1.05x faster                                               |
| pycparser               | 1.17 sec                                               | 1.12 sec: 1.05x faster                                              |
| float                   | 76.3 ms                                                | 72.8 ms: 1.05x faster                                               |
| sqlglot_optimize        | 53.0 ms                                                | 50.7 ms: 1.05x faster                                               |
| deepcopy                | 344 us                                                 | 330 us: 1.04x faster                                                |
| gunicorn                | 1.12 ms                                                | 1.08 ms: 1.04x faster                                               |
| aiohttp                 | 1.05 ms                                                | 1.00 ms: 1.04x faster                                               |
| pidigits                | 199 ms                                                 | 192 ms: 1.04x faster                                                |
| sympy_expand            | 472 ms                                                 | 453 ms: 1.04x faster                                                |
| telco                   | 6.62 ms                                                | 6.37 ms: 1.04x faster                                               |
| sqlglot_normalize       | 108 ms                                                 | 104 ms: 1.04x faster                                                |
| go                      | 143 ms                                                 | 138 ms: 1.04x faster                                                |
| pprint_pformat          | 1.44 sec                                               | 1.39 sec: 1.03x faster                                              |
| docutils                | 2.60 sec                                               | 2.51 sec: 1.03x faster                                              |
| chaos                   | 68.6 ms                                                | 66.4 ms: 1.03x faster                                               |
| pickle_dict             | 31.4 us                                                | 30.5 us: 1.03x faster                                               |
| regex_v8                | 22.3 ms                                                | 21.7 ms: 1.03x faster                                               |
| coroutines              | 26.1 ms                                                | 25.5 ms: 1.02x faster                                               |
| thrift                  | 752 us                                                 | 735 us: 1.02x faster                                                |
| pickle_list             | 4.17 us                                                | 4.09 us: 1.02x faster                                               |
| html5lib                | 63.2 ms                                                | 61.9 ms: 1.02x faster                                               |
| 2to3                    | 257 ms                                                 | 253 ms: 1.02x faster                                                |
| chameleon               | 6.41 ms                                                | 6.29 ms: 1.02x faster                                               |
| pprint_safe_repr        | 691 ms                                                 | 678 ms: 1.02x faster                                                |
| tornado_http            | 96.6 ms                                                | 95.0 ms: 1.02x faster                                               |
| bench_thread_pool       | 810 us                                                 | 800 us: 1.01x faster                                                |
| async_tree_none         | 529 ms                                                 | 523 ms: 1.01x faster                                                |
| unpickle_list           | 4.95 us                                                | 4.90 us: 1.01x faster                                               |
| scimark_monte_carlo     | 68.3 ms                                                | 67.6 ms: 1.01x faster                                               |
| unpack_sequence         | 43.4 ns                                                | 43.0 ns: 1.01x faster                                               |
| xml_etree_process       | 53.8 ms                                                | 53.2 ms: 1.01x faster                                               |
| xml_etree_iterparse     | 103 ms                                                 | 102 ms: 1.01x faster                                                |
| mako                    | 9.85 ms                                                | 9.82 ms: 1.00x faster                                               |
| dulwich_log             | 63.9 ms                                                | 64.3 ms: 1.01x slower                                               |
| django_template         | 32.5 ms                                                | 32.6 ms: 1.01x slower                                               |
| raytrace                | 290 ms                                                 | 292 ms: 1.01x slower                                                |
| scimark_sparse_mat_mult | 4.40 ms                                                | 4.48 ms: 1.02x slower                                               |
| xml_etree_generate      | 76.2 ms                                                | 77.7 ms: 1.02x slower                                               |
| unpickle                | 13.3 us                                                | 13.6 us: 1.02x slower                                               |
| nbody                   | 95.0 ms                                                | 97.9 ms: 1.03x slower                                               |
| regex_dna               | 203 ms                                                 | 210 ms: 1.03x slower                                                |
| async_generators        | 359 ms                                                 | 372 ms: 1.04x slower                                                |
| mdp                     | 2.62 sec                                               | 2.72 sec: 1.04x slower                                              |
| regex_effbot            | 3.36 ms                                                | 3.50 ms: 1.04x slower                                               |
| pathlib                 | 18.2 ms                                                | 19.0 ms: 1.05x slower                                               |
| pickle                  | 9.79 us                                                | 10.3 us: 1.05x slower                                               |
| sqlglot_transpile       | 1.66 ms                                                | 1.78 ms: 1.07x slower                                               |
| python_startup          | 8.36 ms                                                | 8.94 ms: 1.07x slower                                               |
| sqlglot_parse           | 1.37 ms                                                | 1.48 ms: 1.08x slower                                               |
| python_startup_no_site  | 5.96 ms                                                | 6.47 ms: 1.08x slower                                               |
| sqlite_synth            | 2.49 us                                                | 2.70 us: 1.09x slower                                               |
| scimark_sor             | 115 ms                                                 | 125 ms: 1.09x slower                                                |
| pyflate                 | 417 ms                                                 | 467 ms: 1.12x slower                                                |
| generators              | 72.2 ms                                                | 81.0 ms: 1.12x slower                                               |
| scimark_fft             | 329 ms                                                 | 397 ms: 1.21x slower                                                |
| mypy                    | 669 ms                                                 | 807 ms: 1.21x slower                                                |
| crypto_pyaes            | 73.9 ms                                                | 89.5 ms: 1.21x slower                                               |
| spectral_norm           | 99.9 ms                                                | 141 ms: 1.41x slower                                                |
| Geometric mean          | (ref)                                                  | 1.01x faster                                                        |

Benchmark hidden because not significant (7): scimark_lu, deepcopy_reduce, bench_mp_pool, async_tree_cpu_io_mixed, async_tree_io, meteor_contest, async_tree_memoization
Ignored benchmarks (4) of /home/mdboom/Work/builds/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of /home/mdboom/Work/builds/benchmarking/results/bm-20230131-3.12.0a4+-fe65f49/bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-fe65f49.json: asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal
