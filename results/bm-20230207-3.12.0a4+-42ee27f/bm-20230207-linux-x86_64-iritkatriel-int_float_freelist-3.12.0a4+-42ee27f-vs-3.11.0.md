
# Results vs. 3.11.0

- fork: iritkatriel
- ref: int_float_freelist
- machine: linux-x86_64
- commit hash: 42ee27f
- commit date: 2023-02-07
- overall geometric mean: 1.03x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-iritkatriel-int_float_freelist-3.12.0a4+-42ee27f |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 257 ms                                                 | 252 ms: 1.02x faster                                                      |
| chameleon      | 6.41 ms                                                | 6.31 ms: 1.01x faster                                                     |
| docutils       | 2.60 sec                                               | 2.49 sec: 1.04x faster                                                    |
| html5lib       | 63.2 ms                                                | 60.6 ms: 1.04x faster                                                     |
| tornado_http   | 96.6 ms                                                | 94.0 ms: 1.03x faster                                                     |
| Geometric mean | (ref)                                                  | 1.03x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-iritkatriel-int_float_freelist-3.12.0a4+-42ee27f |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 76.3 ms                                                | 72.5 ms: 1.05x faster                                                     |
| pidigits       | 199 ms                                                 | 203 ms: 1.02x slower                                                      |
| nbody          | 95.0 ms                                                | 97.7 ms: 1.03x slower                                                     |
| Geometric mean | (ref)                                                  | 1.00x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-iritkatriel-int_float_freelist-3.12.0a4+-42ee27f |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 129 ms: 1.06x faster                                                      |
| regex_v8       | 22.3 ms                                                | 21.8 ms: 1.02x faster                                                     |
| regex_effbot   | 3.36 ms                                                | 3.43 ms: 1.02x slower                                                     |
| regex_dna      | 203 ms                                                 | 213 ms: 1.05x slower                                                      |
| Geometric mean | (ref)                                                  | 1.00x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-iritkatriel-int_float_freelist-3.12.0a4+-42ee27f |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| json_dumps           | 12.7 ms                                                | 9.43 ms: 1.34x faster                                                     |
| unpickle_pure_python | 225 us                                                 | 197 us: 1.14x faster                                                      |
| json_loads           | 26.2 us                                                | 23.7 us: 1.11x faster                                                     |
| xml_etree_parse      | 158 ms                                                 | 147 ms: 1.07x faster                                                      |
| pickle_pure_python   | 304 us                                                 | 284 us: 1.07x faster                                                      |
| pickle_list          | 4.17 us                                                | 3.98 us: 1.05x faster                                                     |
| unpickle_list        | 4.95 us                                                | 4.84 us: 1.02x faster                                                     |
| pickle_dict          | 31.4 us                                                | 30.8 us: 1.02x faster                                                     |
| pickle               | 9.79 us                                                | 9.98 us: 1.02x slower                                                     |
| xml_etree_generate   | 76.2 ms                                                | 77.9 ms: 1.02x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                              |

Benchmark hidden because not significant (3): unpickle, xml_etree_iterparse, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-iritkatriel-int_float_freelist-3.12.0a4+-42ee27f |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 8.36 ms                                                | 8.97 ms: 1.07x slower                                                     |
| python_startup_no_site | 5.96 ms                                                | 6.49 ms: 1.09x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.08x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-iritkatriel-int_float_freelist-3.12.0a4+-42ee27f |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| genshi_xml      | 52.1 ms                                                | 47.5 ms: 1.10x faster                                                     |
| genshi_text     | 22.1 ms                                                | 20.5 ms: 1.08x faster                                                     |
| mako            | 9.85 ms                                                | 9.63 ms: 1.02x faster                                                     |
| django_template | 32.5 ms                                                | 32.2 ms: 1.01x faster                                                     |
| Geometric mean  | (ref)                                                  | 1.05x faster                                                              |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-iritkatriel-int_float_freelist-3.12.0a4+-42ee27f |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| json_dumps              | 12.7 ms                                                | 9.43 ms: 1.34x faster                                                     |
| unpickle_pure_python    | 225 us                                                 | 197 us: 1.14x faster                                                      |
| deltablue               | 3.64 ms                                                | 3.21 ms: 1.13x faster                                                     |
| richards                | 46.2 ms                                                | 41.4 ms: 1.12x faster                                                     |
| json_loads              | 26.2 us                                                | 23.7 us: 1.11x faster                                                     |
| scimark_sparse_mat_mult | 4.40 ms                                                | 3.99 ms: 1.10x faster                                                     |
| genshi_xml              | 52.1 ms                                                | 47.5 ms: 1.10x faster                                                     |
| logging_silent          | 98.5 ns                                                | 90.7 ns: 1.09x faster                                                     |
| json                    | 4.95 ms                                                | 4.56 ms: 1.09x faster                                                     |
| nqueens                 | 85.0 ms                                                | 78.6 ms: 1.08x faster                                                     |
| scimark_sor             | 115 ms                                                 | 107 ms: 1.08x faster                                                      |
| genshi_text             | 22.1 ms                                                | 20.5 ms: 1.08x faster                                                     |
| logging_simple          | 6.06 us                                                | 5.64 us: 1.08x faster                                                     |
| chaos                   | 68.6 ms                                                | 63.9 ms: 1.07x faster                                                     |
| xml_etree_parse         | 158 ms                                                 | 147 ms: 1.07x faster                                                      |
| pickle_pure_python      | 304 us                                                 | 284 us: 1.07x faster                                                      |
| mdp                     | 2.62 sec                                               | 2.45 sec: 1.07x faster                                                    |
| scimark_fft             | 329 ms                                                 | 308 ms: 1.07x faster                                                      |
| hexiom                  | 6.35 ms                                                | 5.96 ms: 1.07x faster                                                     |
| deepcopy_memo           | 36.4 us                                                | 34.2 us: 1.06x faster                                                     |
| pycparser               | 1.17 sec                                               | 1.10 sec: 1.06x faster                                                    |
| go                      | 143 ms                                                 | 135 ms: 1.06x faster                                                      |
| coroutines              | 26.1 ms                                                | 24.6 ms: 1.06x faster                                                     |
| spectral_norm           | 99.9 ms                                                | 94.4 ms: 1.06x faster                                                     |
| pyflate                 | 417 ms                                                 | 394 ms: 1.06x faster                                                      |
| sympy_sum               | 166 ms                                                 | 157 ms: 1.06x faster                                                      |
| logging_format          | 6.62 us                                                | 6.26 us: 1.06x faster                                                     |
| sympy_str               | 287 ms                                                 | 272 ms: 1.06x faster                                                      |
| regex_compile           | 136 ms                                                 | 129 ms: 1.06x faster                                                      |
| float                   | 76.3 ms                                                | 72.5 ms: 1.05x faster                                                     |
| sympy_integrate         | 20.9 ms                                                | 19.8 ms: 1.05x faster                                                     |
| aiohttp                 | 1.05 ms                                                | 995 us: 1.05x faster                                                      |
| gunicorn                | 1.12 ms                                                | 1.07 ms: 1.05x faster                                                     |
| pickle_list             | 4.17 us                                                | 3.98 us: 1.05x faster                                                     |
| docutils                | 2.60 sec                                               | 2.49 sec: 1.04x faster                                                    |
| html5lib                | 63.2 ms                                                | 60.6 ms: 1.04x faster                                                     |
| deepcopy                | 344 us                                                 | 331 us: 1.04x faster                                                      |
| bench_thread_pool       | 810 us                                                 | 780 us: 1.04x faster                                                      |
| sqlglot_optimize        | 53.0 ms                                                | 51.0 ms: 1.04x faster                                                     |
| coverage                | 101 ms                                                 | 97.1 ms: 1.03x faster                                                     |
| sympy_expand            | 472 ms                                                 | 457 ms: 1.03x faster                                                      |
| unpack_sequence         | 43.4 ns                                                | 42.1 ns: 1.03x faster                                                     |
| telco                   | 6.62 ms                                                | 6.42 ms: 1.03x faster                                                     |
| pathlib                 | 18.2 ms                                                | 17.6 ms: 1.03x faster                                                     |
| pprint_pformat          | 1.44 sec                                               | 1.40 sec: 1.03x faster                                                    |
| fannkuch                | 388 ms                                                 | 377 ms: 1.03x faster                                                      |
| dulwich_log             | 63.9 ms                                                | 62.1 ms: 1.03x faster                                                     |
| tornado_http            | 96.6 ms                                                | 94.0 ms: 1.03x faster                                                     |
| unpickle_list           | 4.95 us                                                | 4.84 us: 1.02x faster                                                     |
| 2to3                    | 257 ms                                                 | 252 ms: 1.02x faster                                                      |
| mako                    | 9.85 ms                                                | 9.63 ms: 1.02x faster                                                     |
| raytrace                | 290 ms                                                 | 284 ms: 1.02x faster                                                      |
| regex_v8                | 22.3 ms                                                | 21.8 ms: 1.02x faster                                                     |
| deepcopy_reduce         | 2.97 us                                                | 2.91 us: 1.02x faster                                                     |
| pickle_dict             | 31.4 us                                                | 30.8 us: 1.02x faster                                                     |
| async_generators        | 359 ms                                                 | 353 ms: 1.02x faster                                                      |
| sqlglot_normalize       | 108 ms                                                 | 106 ms: 1.02x faster                                                      |
| pprint_safe_repr        | 691 ms                                                 | 680 ms: 1.02x faster                                                      |
| thrift                  | 752 us                                                 | 740 us: 1.02x faster                                                      |
| chameleon               | 6.41 ms                                                | 6.31 ms: 1.01x faster                                                     |
| django_template         | 32.5 ms                                                | 32.2 ms: 1.01x faster                                                     |
| scimark_monte_carlo     | 68.3 ms                                                | 67.7 ms: 1.01x faster                                                     |
| meteor_contest          | 105 ms                                                 | 106 ms: 1.01x slower                                                      |
| async_tree_io           | 1.31 sec                                               | 1.32 sec: 1.01x slower                                                    |
| async_tree_cpu_io_mixed | 752 ms                                                 | 761 ms: 1.01x slower                                                      |
| pidigits                | 199 ms                                                 | 203 ms: 1.02x slower                                                      |
| pickle                  | 9.79 us                                                | 9.98 us: 1.02x slower                                                     |
| xml_etree_generate      | 76.2 ms                                                | 77.9 ms: 1.02x slower                                                     |
| regex_effbot            | 3.36 ms                                                | 3.43 ms: 1.02x slower                                                     |
| sqlglot_transpile       | 1.66 ms                                                | 1.70 ms: 1.03x slower                                                     |
| crypto_pyaes            | 73.9 ms                                                | 75.9 ms: 1.03x slower                                                     |
| nbody                   | 95.0 ms                                                | 97.7 ms: 1.03x slower                                                     |
| sqlite_synth            | 2.49 us                                                | 2.57 us: 1.03x slower                                                     |
| sqlglot_parse           | 1.37 ms                                                | 1.41 ms: 1.03x slower                                                     |
| regex_dna               | 203 ms                                                 | 213 ms: 1.05x slower                                                      |
| async_tree_memoization  | 625 ms                                                 | 660 ms: 1.06x slower                                                      |
| generators              | 72.2 ms                                                | 77.0 ms: 1.07x slower                                                     |
| python_startup          | 8.36 ms                                                | 8.97 ms: 1.07x slower                                                     |
| python_startup_no_site  | 5.96 ms                                                | 6.49 ms: 1.09x slower                                                     |
| mypy                    | 669 ms                                                 | 808 ms: 1.21x slower                                                      |
| Geometric mean          | (ref)                                                  | 1.03x faster                                                              |

Benchmark hidden because not significant (6): unpickle, async_tree_none, xml_etree_iterparse, xml_etree_process, bench_mp_pool, scimark_lu
Ignored benchmarks (4) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20230207-3.12.0a4+-42ee27f/bm-20230207-linux-x86_64-iritkatriel-int_float_freelist-3.12.0a4+-42ee27f.json: asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal
