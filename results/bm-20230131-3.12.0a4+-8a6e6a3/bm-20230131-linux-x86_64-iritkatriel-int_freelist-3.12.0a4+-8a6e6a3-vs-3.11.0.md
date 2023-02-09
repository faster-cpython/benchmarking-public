
# Results vs. 3.11.0

- fork: iritkatriel
- ref: int_freelist
- machine: linux-x86_64
- commit hash: 8a6e6a3
- commit date: 2023-01-31
- overall geometric mean: 1.01x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-8a6e6a3 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 257 ms                                                 | 252 ms: 1.02x faster                                                |
| chameleon      | 6.41 ms                                                | 6.37 ms: 1.01x faster                                               |
| docutils       | 2.60 sec                                               | 2.50 sec: 1.04x faster                                              |
| html5lib       | 63.2 ms                                                | 61.6 ms: 1.03x faster                                               |
| tornado_http   | 96.6 ms                                                | 95.3 ms: 1.01x faster                                               |
| Geometric mean | (ref)                                                  | 1.02x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-8a6e6a3 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| pidigits       | 199 ms                                                 | 192 ms: 1.04x faster                                                |
| float          | 76.3 ms                                                | 73.8 ms: 1.03x faster                                               |
| nbody          | 95.0 ms                                                | 96.3 ms: 1.01x slower                                               |
| Geometric mean | (ref)                                                  | 1.02x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-8a6e6a3 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 127 ms: 1.07x faster                                                |
| regex_v8       | 22.3 ms                                                | 21.2 ms: 1.05x faster                                               |
| regex_dna      | 203 ms                                                 | 208 ms: 1.02x slower                                                |
| regex_effbot   | 3.36 ms                                                | 3.47 ms: 1.03x slower                                               |
| Geometric mean | (ref)                                                  | 1.02x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-8a6e6a3 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| json_dumps           | 12.7 ms                                                | 9.50 ms: 1.33x faster                                               |
| unpickle_pure_python | 225 us                                                 | 198 us: 1.14x faster                                                |
| xml_etree_parse      | 158 ms                                                 | 147 ms: 1.08x faster                                                |
| json_loads           | 26.2 us                                                | 24.7 us: 1.06x faster                                               |
| pickle_pure_python   | 304 us                                                 | 286 us: 1.06x faster                                                |
| unpickle_list        | 4.95 us                                                | 4.93 us: 1.01x faster                                               |
| pickle_dict          | 31.4 us                                                | 31.8 us: 1.01x slower                                               |
| pickle_list          | 4.17 us                                                | 4.23 us: 1.01x slower                                               |
| xml_etree_generate   | 76.2 ms                                                | 77.4 ms: 1.02x slower                                               |
| pickle               | 9.79 us                                                | 10.1 us: 1.03x slower                                               |
| unpickle             | 13.3 us                                                | 14.0 us: 1.06x slower                                               |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                        |

Benchmark hidden because not significant (2): xml_etree_process, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-8a6e6a3 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 8.36 ms                                                | 8.97 ms: 1.07x slower                                               |
| python_startup_no_site | 5.96 ms                                                | 6.49 ms: 1.09x slower                                               |
| Geometric mean         | (ref)                                                  | 1.08x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-8a6e6a3 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_xml      | 52.1 ms                                                | 47.4 ms: 1.10x faster                                               |
| genshi_text     | 22.1 ms                                                | 20.6 ms: 1.07x faster                                               |
| mako            | 9.85 ms                                                | 9.80 ms: 1.01x faster                                               |
| django_template | 32.5 ms                                                | 33.1 ms: 1.02x slower                                               |
| Geometric mean  | (ref)                                                  | 1.04x faster                                                        |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-8a6e6a3 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| json_dumps              | 12.7 ms                                                | 9.50 ms: 1.33x faster                                               |
| unpickle_pure_python    | 225 us                                                 | 198 us: 1.14x faster                                                |
| deltablue               | 3.64 ms                                                | 3.25 ms: 1.12x faster                                               |
| nqueens                 | 85.0 ms                                                | 76.2 ms: 1.12x faster                                               |
| genshi_xml              | 52.1 ms                                                | 47.4 ms: 1.10x faster                                               |
| fannkuch                | 388 ms                                                 | 360 ms: 1.08x faster                                                |
| xml_etree_parse         | 158 ms                                                 | 147 ms: 1.08x faster                                                |
| regex_compile           | 136 ms                                                 | 127 ms: 1.07x faster                                                |
| genshi_text             | 22.1 ms                                                | 20.6 ms: 1.07x faster                                               |
| go                      | 143 ms                                                 | 134 ms: 1.07x faster                                                |
| richards                | 46.2 ms                                                | 43.2 ms: 1.07x faster                                               |
| sympy_sum               | 166 ms                                                 | 156 ms: 1.07x faster                                                |
| chaos                   | 68.6 ms                                                | 64.4 ms: 1.07x faster                                               |
| logging_silent          | 98.5 ns                                                | 92.4 ns: 1.07x faster                                               |
| json_loads              | 26.2 us                                                | 24.7 us: 1.06x faster                                               |
| hexiom                  | 6.35 ms                                                | 5.98 ms: 1.06x faster                                               |
| pickle_pure_python      | 304 us                                                 | 286 us: 1.06x faster                                                |
| sympy_integrate         | 20.9 ms                                                | 19.7 ms: 1.06x faster                                               |
| sympy_str               | 287 ms                                                 | 271 ms: 1.06x faster                                                |
| json                    | 4.95 ms                                                | 4.69 ms: 1.06x faster                                               |
| pprint_pformat          | 1.44 sec                                               | 1.37 sec: 1.06x faster                                              |
| regex_v8                | 22.3 ms                                                | 21.2 ms: 1.05x faster                                               |
| pycparser               | 1.17 sec                                               | 1.12 sec: 1.05x faster                                              |
| logging_simple          | 6.06 us                                                | 5.79 us: 1.05x faster                                               |
| coverage                | 101 ms                                                 | 96.1 ms: 1.05x faster                                               |
| sqlglot_optimize        | 53.0 ms                                                | 50.8 ms: 1.04x faster                                               |
| deepcopy_memo           | 36.4 us                                                | 34.9 us: 1.04x faster                                               |
| logging_format          | 6.62 us                                                | 6.35 us: 1.04x faster                                               |
| pidigits                | 199 ms                                                 | 192 ms: 1.04x faster                                                |
| gunicorn                | 1.12 ms                                                | 1.08 ms: 1.04x faster                                               |
| aiohttp                 | 1.05 ms                                                | 1.00 ms: 1.04x faster                                               |
| docutils                | 2.60 sec                                               | 2.50 sec: 1.04x faster                                              |
| deepcopy                | 344 us                                                 | 331 us: 1.04x faster                                                |
| mdp                     | 2.62 sec                                               | 2.53 sec: 1.04x faster                                              |
| sqlglot_normalize       | 108 ms                                                 | 104 ms: 1.03x faster                                                |
| float                   | 76.3 ms                                                | 73.8 ms: 1.03x faster                                               |
| pprint_safe_repr        | 691 ms                                                 | 669 ms: 1.03x faster                                                |
| coroutines              | 26.1 ms                                                | 25.3 ms: 1.03x faster                                               |
| telco                   | 6.62 ms                                                | 6.43 ms: 1.03x faster                                               |
| sympy_expand            | 472 ms                                                 | 459 ms: 1.03x faster                                                |
| scimark_monte_carlo     | 68.3 ms                                                | 66.4 ms: 1.03x faster                                               |
| html5lib                | 63.2 ms                                                | 61.6 ms: 1.03x faster                                               |
| 2to3                    | 257 ms                                                 | 252 ms: 1.02x faster                                                |
| unpack_sequence         | 43.4 ns                                                | 42.7 ns: 1.02x faster                                               |
| tornado_http            | 96.6 ms                                                | 95.3 ms: 1.01x faster                                               |
| bench_thread_pool       | 810 us                                                 | 801 us: 1.01x faster                                                |
| chameleon               | 6.41 ms                                                | 6.37 ms: 1.01x faster                                               |
| unpickle_list           | 4.95 us                                                | 4.93 us: 1.01x faster                                               |
| mako                    | 9.85 ms                                                | 9.80 ms: 1.01x faster                                               |
| dulwich_log             | 63.9 ms                                                | 64.4 ms: 1.01x slower                                               |
| pickle_dict             | 31.4 us                                                | 31.8 us: 1.01x slower                                               |
| async_tree_cpu_io_mixed | 752 ms                                                 | 761 ms: 1.01x slower                                                |
| nbody                   | 95.0 ms                                                | 96.3 ms: 1.01x slower                                               |
| pickle_list             | 4.17 us                                                | 4.23 us: 1.01x slower                                               |
| xml_etree_generate      | 76.2 ms                                                | 77.4 ms: 1.02x slower                                               |
| async_tree_io           | 1.31 sec                                               | 1.33 sec: 1.02x slower                                              |
| deepcopy_reduce         | 2.97 us                                                | 3.02 us: 1.02x slower                                               |
| django_template         | 32.5 ms                                                | 33.1 ms: 1.02x slower                                               |
| regex_dna               | 203 ms                                                 | 208 ms: 1.02x slower                                                |
| async_generators        | 359 ms                                                 | 369 ms: 1.03x slower                                                |
| regex_effbot            | 3.36 ms                                                | 3.47 ms: 1.03x slower                                               |
| scimark_sparse_mat_mult | 4.40 ms                                                | 4.55 ms: 1.03x slower                                               |
| pickle                  | 9.79 us                                                | 10.1 us: 1.03x slower                                               |
| pathlib                 | 18.2 ms                                                | 18.9 ms: 1.04x slower                                               |
| async_tree_memoization  | 625 ms                                                 | 659 ms: 1.06x slower                                                |
| unpickle                | 13.3 us                                                | 14.0 us: 1.06x slower                                               |
| scimark_sor             | 115 ms                                                 | 123 ms: 1.07x slower                                                |
| sqlglot_transpile       | 1.66 ms                                                | 1.78 ms: 1.07x slower                                               |
| python_startup          | 8.36 ms                                                | 8.97 ms: 1.07x slower                                               |
| sqlite_synth            | 2.49 us                                                | 2.68 us: 1.08x slower                                               |
| sqlglot_parse           | 1.37 ms                                                | 1.48 ms: 1.08x slower                                               |
| python_startup_no_site  | 5.96 ms                                                | 6.49 ms: 1.09x slower                                               |
| pyflate                 | 417 ms                                                 | 461 ms: 1.11x slower                                                |
| generators              | 72.2 ms                                                | 83.5 ms: 1.16x slower                                               |
| scimark_fft             | 329 ms                                                 | 390 ms: 1.18x slower                                                |
| mypy                    | 669 ms                                                 | 805 ms: 1.20x slower                                                |
| crypto_pyaes            | 73.9 ms                                                | 90.0 ms: 1.22x slower                                               |
| spectral_norm           | 99.9 ms                                                | 138 ms: 1.38x slower                                                |
| Geometric mean          | (ref)                                                  | 1.01x faster                                                        |

Benchmark hidden because not significant (8): meteor_contest, scimark_lu, async_tree_none, xml_etree_process, thrift, bench_mp_pool, xml_etree_iterparse, raytrace
Ignored benchmarks (4) of /home/mdboom/Work/builds/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of /home/mdboom/Work/builds/benchmarking/results/bm-20230131-3.12.0a4+-8a6e6a3/bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-8a6e6a3.json: asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal
