
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
| 2to3           | 257 ms                                                 | 252 ms: 1.02x faster                                                |
| chameleon      | 6.41 ms                                                | 6.35 ms: 1.01x faster                                               |
| docutils       | 2.60 sec                                               | 2.51 sec: 1.03x faster                                              |
| html5lib       | 63.2 ms                                                | 62.1 ms: 1.02x faster                                               |
| tornado_http   | 96.6 ms                                                | 95.0 ms: 1.02x faster                                               |
| Geometric mean | (ref)                                                  | 1.02x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-fe65f49 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 76.3 ms                                                | 72.0 ms: 1.06x faster                                               |
| pidigits       | 199 ms                                                 | 199 ms: 1.00x faster                                                |
| nbody          | 95.0 ms                                                | 97.5 ms: 1.03x slower                                               |
| Geometric mean | (ref)                                                  | 1.01x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-fe65f49 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 128 ms: 1.06x faster                                                |
| regex_v8       | 22.3 ms                                                | 22.2 ms: 1.00x faster                                               |
| regex_dna      | 203 ms                                                 | 210 ms: 1.03x slower                                                |
| regex_effbot   | 3.36 ms                                                | 3.63 ms: 1.08x slower                                               |
| Geometric mean | (ref)                                                  | 1.01x slower                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-fe65f49 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| json_dumps           | 12.7 ms                                                | 9.52 ms: 1.33x faster                                               |
| unpickle_pure_python | 225 us                                                 | 199 us: 1.13x faster                                                |
| xml_etree_parse      | 158 ms                                                 | 147 ms: 1.08x faster                                                |
| pickle_pure_python   | 304 us                                                 | 286 us: 1.06x faster                                                |
| json_loads           | 26.2 us                                                | 24.9 us: 1.06x faster                                               |
| unpickle_list        | 4.95 us                                                | 4.85 us: 1.02x faster                                               |
| xml_etree_process    | 53.8 ms                                                | 53.5 ms: 1.01x faster                                               |
| xml_etree_iterparse  | 103 ms                                                 | 102 ms: 1.00x faster                                                |
| xml_etree_generate   | 76.2 ms                                                | 77.6 ms: 1.02x slower                                               |
| pickle_dict          | 31.4 us                                                | 32.1 us: 1.02x slower                                               |
| pickle_list          | 4.17 us                                                | 4.30 us: 1.03x slower                                               |
| unpickle             | 13.3 us                                                | 13.8 us: 1.04x slower                                               |
| pickle               | 9.79 us                                                | 10.2 us: 1.05x slower                                               |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-fe65f49 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 8.36 ms                                                | 8.91 ms: 1.07x slower                                               |
| python_startup_no_site | 5.96 ms                                                | 6.44 ms: 1.08x slower                                               |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-fe65f49 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_xml      | 52.1 ms                                                | 46.9 ms: 1.11x faster                                               |
| genshi_text     | 22.1 ms                                                | 21.0 ms: 1.05x faster                                               |
| django_template | 32.5 ms                                                | 32.7 ms: 1.01x slower                                               |
| Geometric mean  | (ref)                                                  | 1.04x faster                                                        |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-fe65f49 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| json_dumps              | 12.7 ms                                                | 9.52 ms: 1.33x faster                                               |
| nqueens                 | 85.0 ms                                                | 74.8 ms: 1.14x faster                                               |
| unpickle_pure_python    | 225 us                                                 | 199 us: 1.13x faster                                                |
| deltablue               | 3.64 ms                                                | 3.24 ms: 1.13x faster                                               |
| genshi_xml              | 52.1 ms                                                | 46.9 ms: 1.11x faster                                               |
| logging_silent          | 98.5 ns                                                | 90.9 ns: 1.08x faster                                               |
| xml_etree_parse         | 158 ms                                                 | 147 ms: 1.08x faster                                                |
| sympy_sum               | 166 ms                                                 | 154 ms: 1.08x faster                                                |
| logging_simple          | 6.06 us                                                | 5.64 us: 1.07x faster                                               |
| chaos                   | 68.6 ms                                                | 63.9 ms: 1.07x faster                                               |
| sympy_str               | 287 ms                                                 | 268 ms: 1.07x faster                                                |
| sympy_integrate         | 20.9 ms                                                | 19.6 ms: 1.06x faster                                               |
| regex_compile           | 136 ms                                                 | 128 ms: 1.06x faster                                                |
| pickle_pure_python      | 304 us                                                 | 286 us: 1.06x faster                                                |
| go                      | 143 ms                                                 | 135 ms: 1.06x faster                                                |
| float                   | 76.3 ms                                                | 72.0 ms: 1.06x faster                                               |
| richards                | 46.2 ms                                                | 43.6 ms: 1.06x faster                                               |
| logging_format          | 6.62 us                                                | 6.26 us: 1.06x faster                                               |
| json_loads              | 26.2 us                                                | 24.9 us: 1.06x faster                                               |
| hexiom                  | 6.35 ms                                                | 6.02 ms: 1.06x faster                                               |
| fannkuch                | 388 ms                                                 | 368 ms: 1.05x faster                                                |
| json                    | 4.95 ms                                                | 4.70 ms: 1.05x faster                                               |
| genshi_text             | 22.1 ms                                                | 21.0 ms: 1.05x faster                                               |
| coverage                | 101 ms                                                 | 95.6 ms: 1.05x faster                                               |
| pprint_pformat          | 1.44 sec                                               | 1.37 sec: 1.05x faster                                              |
| aiohttp                 | 1.05 ms                                                | 1.00 ms: 1.05x faster                                               |
| gunicorn                | 1.12 ms                                                | 1.08 ms: 1.04x faster                                               |
| sympy_expand            | 472 ms                                                 | 453 ms: 1.04x faster                                                |
| pprint_safe_repr        | 691 ms                                                 | 663 ms: 1.04x faster                                                |
| sqlglot_optimize        | 53.0 ms                                                | 51.0 ms: 1.04x faster                                               |
| deepcopy                | 344 us                                                 | 331 us: 1.04x faster                                                |
| deepcopy_memo           | 36.4 us                                                | 35.2 us: 1.04x faster                                               |
| docutils                | 2.60 sec                                               | 2.51 sec: 1.03x faster                                              |
| unpack_sequence         | 43.4 ns                                                | 42.0 ns: 1.03x faster                                               |
| telco                   | 6.62 ms                                                | 6.43 ms: 1.03x faster                                               |
| sqlglot_normalize       | 108 ms                                                 | 105 ms: 1.03x faster                                                |
| scimark_monte_carlo     | 68.3 ms                                                | 66.7 ms: 1.02x faster                                               |
| coroutines              | 26.1 ms                                                | 25.5 ms: 1.02x faster                                               |
| 2to3                    | 257 ms                                                 | 252 ms: 1.02x faster                                                |
| unpickle_list           | 4.95 us                                                | 4.85 us: 1.02x faster                                               |
| html5lib                | 63.2 ms                                                | 62.1 ms: 1.02x faster                                               |
| meteor_contest          | 105 ms                                                 | 103 ms: 1.02x faster                                                |
| tornado_http            | 96.6 ms                                                | 95.0 ms: 1.02x faster                                               |
| async_tree_none         | 529 ms                                                 | 522 ms: 1.01x faster                                                |
| thrift                  | 752 us                                                 | 743 us: 1.01x faster                                                |
| chameleon               | 6.41 ms                                                | 6.35 ms: 1.01x faster                                               |
| scimark_lu              | 107 ms                                                 | 107 ms: 1.01x faster                                                |
| bench_thread_pool       | 810 us                                                 | 805 us: 1.01x faster                                                |
| xml_etree_process       | 53.8 ms                                                | 53.5 ms: 1.01x faster                                               |
| xml_etree_iterparse     | 103 ms                                                 | 102 ms: 1.00x faster                                                |
| regex_v8                | 22.3 ms                                                | 22.2 ms: 1.00x faster                                               |
| pidigits                | 199 ms                                                 | 199 ms: 1.00x faster                                                |
| async_tree_cpu_io_mixed | 752 ms                                                 | 757 ms: 1.01x slower                                                |
| django_template         | 32.5 ms                                                | 32.7 ms: 1.01x slower                                               |
| dulwich_log             | 63.9 ms                                                | 64.5 ms: 1.01x slower                                               |
| mdp                     | 2.62 sec                                               | 2.66 sec: 1.02x slower                                              |
| xml_etree_generate      | 76.2 ms                                                | 77.6 ms: 1.02x slower                                               |
| pickle_dict             | 31.4 us                                                | 32.1 us: 1.02x slower                                               |
| scimark_sparse_mat_mult | 4.40 ms                                                | 4.52 ms: 1.03x slower                                               |
| nbody                   | 95.0 ms                                                | 97.5 ms: 1.03x slower                                               |
| async_tree_memoization  | 625 ms                                                 | 644 ms: 1.03x slower                                                |
| pickle_list             | 4.17 us                                                | 4.30 us: 1.03x slower                                               |
| async_generators        | 359 ms                                                 | 371 ms: 1.03x slower                                                |
| regex_dna               | 203 ms                                                 | 210 ms: 1.03x slower                                                |
| pathlib                 | 18.2 ms                                                | 18.9 ms: 1.04x slower                                               |
| unpickle                | 13.3 us                                                | 13.8 us: 1.04x slower                                               |
| pickle                  | 9.79 us                                                | 10.2 us: 1.05x slower                                               |
| sqlglot_transpile       | 1.66 ms                                                | 1.77 ms: 1.06x slower                                               |
| python_startup          | 8.36 ms                                                | 8.91 ms: 1.07x slower                                               |
| sqlite_synth            | 2.49 us                                                | 2.67 us: 1.07x slower                                               |
| sqlglot_parse           | 1.37 ms                                                | 1.47 ms: 1.07x slower                                               |
| python_startup_no_site  | 5.96 ms                                                | 6.44 ms: 1.08x slower                                               |
| regex_effbot            | 3.36 ms                                                | 3.63 ms: 1.08x slower                                               |
| scimark_sor             | 115 ms                                                 | 125 ms: 1.08x slower                                                |
| pyflate                 | 417 ms                                                 | 468 ms: 1.12x slower                                                |
| generators              | 72.2 ms                                                | 82.2 ms: 1.14x slower                                               |
| scimark_fft             | 329 ms                                                 | 383 ms: 1.16x slower                                                |
| mypy                    | 669 ms                                                 | 806 ms: 1.21x slower                                                |
| crypto_pyaes            | 73.9 ms                                                | 89.6 ms: 1.21x slower                                               |
| spectral_norm           | 99.9 ms                                                | 136 ms: 1.36x slower                                                |
| Geometric mean          | (ref)                                                  | 1.01x faster                                                        |

Benchmark hidden because not significant (6): mako, bench_mp_pool, raytrace, async_tree_io, deepcopy_reduce, pycparser
Ignored benchmarks (4) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20230131-3.12.0a4+-fe65f49/bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-fe65f49.json: asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal
