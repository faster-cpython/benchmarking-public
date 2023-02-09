
# Results vs. 3.11.0

- fork: iritkatriel
- ref: int_freelist
- machine: linux-x86_64
- commit hash: 906fc0d
- commit date: 2023-01-30
- overall geometric mean: 1.02x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230130-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-906fc0d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 257 ms                                                 | 253 ms: 1.02x faster                                                |
| chameleon      | 6.41 ms                                                | 6.31 ms: 1.02x faster                                               |
| docutils       | 2.60 sec                                               | 2.49 sec: 1.04x faster                                              |
| html5lib       | 63.2 ms                                                | 60.3 ms: 1.05x faster                                               |
| tornado_http   | 96.6 ms                                                | 93.9 ms: 1.03x faster                                               |
| Geometric mean | (ref)                                                  | 1.03x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230130-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-906fc0d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 76.3 ms                                                | 72.1 ms: 1.06x faster                                               |
| pidigits       | 199 ms                                                 | 199 ms: 1.00x faster                                                |
| Geometric mean | (ref)                                                  | 1.02x faster                                                        |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230130-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-906fc0d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 128 ms: 1.06x faster                                                |
| regex_v8       | 22.3 ms                                                | 21.7 ms: 1.03x faster                                               |
| regex_dna      | 203 ms                                                 | 209 ms: 1.03x slower                                                |
| regex_effbot   | 3.36 ms                                                | 3.63 ms: 1.08x slower                                               |
| Geometric mean | (ref)                                                  | 1.01x slower                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230130-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-906fc0d |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| json_dumps           | 12.7 ms                                                | 9.58 ms: 1.32x faster                                               |
| unpickle_pure_python | 225 us                                                 | 197 us: 1.14x faster                                                |
| json_loads           | 26.2 us                                                | 24.2 us: 1.08x faster                                               |
| xml_etree_parse      | 158 ms                                                 | 149 ms: 1.06x faster                                                |
| pickle_pure_python   | 304 us                                                 | 287 us: 1.06x faster                                                |
| unpickle_list        | 4.95 us                                                | 4.89 us: 1.01x faster                                               |
| pickle_dict          | 31.4 us                                                | 31.2 us: 1.01x faster                                               |
| xml_etree_process    | 53.8 ms                                                | 53.5 ms: 1.00x faster                                               |
| pickle_list          | 4.17 us                                                | 4.24 us: 1.02x slower                                               |
| xml_etree_generate   | 76.2 ms                                                | 77.6 ms: 1.02x slower                                               |
| pickle               | 9.79 us                                                | 10.2 us: 1.04x slower                                               |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                        |

Benchmark hidden because not significant (2): unpickle, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230130-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-906fc0d |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 8.36 ms                                                | 8.98 ms: 1.07x slower                                               |
| python_startup_no_site | 5.96 ms                                                | 6.49 ms: 1.09x slower                                               |
| Geometric mean         | (ref)                                                  | 1.08x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230130-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-906fc0d |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_xml      | 52.1 ms                                                | 47.6 ms: 1.09x faster                                               |
| genshi_text     | 22.1 ms                                                | 21.0 ms: 1.05x faster                                               |
| django_template | 32.5 ms                                                | 33.1 ms: 1.02x slower                                               |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                        |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230130-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-906fc0d |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| json_dumps              | 12.7 ms                                                | 9.58 ms: 1.32x faster                                               |
| unpickle_pure_python    | 225 us                                                 | 197 us: 1.14x faster                                                |
| deltablue               | 3.64 ms                                                | 3.20 ms: 1.14x faster                                               |
| richards                | 46.2 ms                                                | 41.6 ms: 1.11x faster                                               |
| scimark_sparse_mat_mult | 4.40 ms                                                | 4.02 ms: 1.10x faster                                               |
| genshi_xml              | 52.1 ms                                                | 47.6 ms: 1.09x faster                                               |
| json_loads              | 26.2 us                                                | 24.2 us: 1.08x faster                                               |
| fannkuch                | 388 ms                                                 | 358 ms: 1.08x faster                                                |
| chaos                   | 68.6 ms                                                | 63.9 ms: 1.07x faster                                               |
| nqueens                 | 85.0 ms                                                | 79.5 ms: 1.07x faster                                               |
| logging_silent          | 98.5 ns                                                | 92.2 ns: 1.07x faster                                               |
| logging_simple          | 6.06 us                                                | 5.68 us: 1.07x faster                                               |
| sympy_sum               | 166 ms                                                 | 156 ms: 1.07x faster                                                |
| go                      | 143 ms                                                 | 134 ms: 1.07x faster                                                |
| sympy_str               | 287 ms                                                 | 270 ms: 1.06x faster                                                |
| hexiom                  | 6.35 ms                                                | 5.97 ms: 1.06x faster                                               |
| xml_etree_parse         | 158 ms                                                 | 149 ms: 1.06x faster                                                |
| regex_compile           | 136 ms                                                 | 128 ms: 1.06x faster                                                |
| json                    | 4.95 ms                                                | 4.67 ms: 1.06x faster                                               |
| scimark_fft             | 329 ms                                                 | 311 ms: 1.06x faster                                                |
| float                   | 76.3 ms                                                | 72.1 ms: 1.06x faster                                               |
| pickle_pure_python      | 304 us                                                 | 287 us: 1.06x faster                                                |
| sympy_integrate         | 20.9 ms                                                | 19.8 ms: 1.06x faster                                               |
| genshi_text             | 22.1 ms                                                | 21.0 ms: 1.05x faster                                               |
| pyflate                 | 417 ms                                                 | 396 ms: 1.05x faster                                                |
| pycparser               | 1.17 sec                                               | 1.12 sec: 1.05x faster                                              |
| deepcopy_memo           | 36.4 us                                                | 34.6 us: 1.05x faster                                               |
| logging_format          | 6.62 us                                                | 6.30 us: 1.05x faster                                               |
| aiohttp                 | 1.05 ms                                                | 997 us: 1.05x faster                                                |
| gunicorn                | 1.12 ms                                                | 1.07 ms: 1.05x faster                                               |
| html5lib                | 63.2 ms                                                | 60.3 ms: 1.05x faster                                               |
| coverage                | 101 ms                                                 | 96.0 ms: 1.05x faster                                               |
| pprint_pformat          | 1.44 sec                                               | 1.38 sec: 1.04x faster                                              |
| sympy_expand            | 472 ms                                                 | 453 ms: 1.04x faster                                                |
| deepcopy                | 344 us                                                 | 330 us: 1.04x faster                                                |
| docutils                | 2.60 sec                                               | 2.49 sec: 1.04x faster                                              |
| scimark_sor             | 115 ms                                                 | 111 ms: 1.04x faster                                                |
| telco                   | 6.62 ms                                                | 6.38 ms: 1.04x faster                                               |
| coroutines              | 26.1 ms                                                | 25.1 ms: 1.04x faster                                               |
| sqlglot_optimize        | 53.0 ms                                                | 51.2 ms: 1.04x faster                                               |
| pprint_safe_repr        | 691 ms                                                 | 669 ms: 1.03x faster                                                |
| tornado_http            | 96.6 ms                                                | 93.9 ms: 1.03x faster                                               |
| regex_v8                | 22.3 ms                                                | 21.7 ms: 1.03x faster                                               |
| bench_thread_pool       | 810 us                                                 | 790 us: 1.03x faster                                                |
| scimark_monte_carlo     | 68.3 ms                                                | 66.7 ms: 1.02x faster                                               |
| sqlglot_normalize       | 108 ms                                                 | 105 ms: 1.02x faster                                                |
| pathlib                 | 18.2 ms                                                | 17.8 ms: 1.02x faster                                               |
| dulwich_log             | 63.9 ms                                                | 62.8 ms: 1.02x faster                                               |
| async_generators        | 359 ms                                                 | 353 ms: 1.02x faster                                                |
| 2to3                    | 257 ms                                                 | 253 ms: 1.02x faster                                                |
| chameleon               | 6.41 ms                                                | 6.31 ms: 1.02x faster                                               |
| unpickle_list           | 4.95 us                                                | 4.89 us: 1.01x faster                                               |
| scimark_lu              | 107 ms                                                 | 106 ms: 1.01x faster                                                |
| thrift                  | 752 us                                                 | 742 us: 1.01x faster                                                |
| deepcopy_reduce         | 2.97 us                                                | 2.94 us: 1.01x faster                                               |
| pickle_dict             | 31.4 us                                                | 31.2 us: 1.01x faster                                               |
| xml_etree_process       | 53.8 ms                                                | 53.5 ms: 1.00x faster                                               |
| pidigits                | 199 ms                                                 | 199 ms: 1.00x faster                                                |
| pickle_list             | 4.17 us                                                | 4.24 us: 1.02x slower                                               |
| xml_etree_generate      | 76.2 ms                                                | 77.6 ms: 1.02x slower                                               |
| django_template         | 32.5 ms                                                | 33.1 ms: 1.02x slower                                               |
| meteor_contest          | 105 ms                                                 | 107 ms: 1.02x slower                                                |
| sqlglot_parse           | 1.37 ms                                                | 1.41 ms: 1.03x slower                                               |
| crypto_pyaes            | 73.9 ms                                                | 76.0 ms: 1.03x slower                                               |
| sqlglot_transpile       | 1.66 ms                                                | 1.71 ms: 1.03x slower                                               |
| regex_dna               | 203 ms                                                 | 209 ms: 1.03x slower                                                |
| pickle                  | 9.79 us                                                | 10.2 us: 1.04x slower                                               |
| sqlite_synth            | 2.49 us                                                | 2.60 us: 1.05x slower                                               |
| spectral_norm           | 99.9 ms                                                | 105 ms: 1.05x slower                                                |
| async_tree_memoization  | 625 ms                                                 | 658 ms: 1.05x slower                                                |
| python_startup          | 8.36 ms                                                | 8.98 ms: 1.07x slower                                               |
| generators              | 72.2 ms                                                | 78.0 ms: 1.08x slower                                               |
| regex_effbot            | 3.36 ms                                                | 3.63 ms: 1.08x slower                                               |
| python_startup_no_site  | 5.96 ms                                                | 6.49 ms: 1.09x slower                                               |
| mypy                    | 669 ms                                                 | 807 ms: 1.21x slower                                                |
| Geometric mean          | (ref)                                                  | 1.02x faster                                                        |

Benchmark hidden because not significant (11): async_tree_none, unpickle, raytrace, unpack_sequence, mdp, xml_etree_iterparse, bench_mp_pool, async_tree_cpu_io_mixed, mako, nbody, async_tree_io
Ignored benchmarks (4) of /home/mdboom/Work/builds/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of /home/mdboom/Work/builds/benchmarking/results/bm-20230130-3.12.0a4+-906fc0d/bm-20230130-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-906fc0d.json: asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal
