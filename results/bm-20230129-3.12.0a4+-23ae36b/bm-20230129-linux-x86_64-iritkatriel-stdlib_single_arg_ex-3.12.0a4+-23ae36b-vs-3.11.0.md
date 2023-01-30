
# Results vs. 3.11.0

- fork: iritkatriel
- ref: stdlib_single_arg_ex
- machine: linux-x86_64
- commit hash: 23ae36b
- commit date: 2023-01-29
- overall geometric mean: 1.03x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230129-linux-x86_64-iritkatriel-stdlib_single_arg_ex-3.12.0a4+-23ae36b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 257 ms                                                 | 251 ms: 1.02x faster                                                        |
| chameleon      | 6.41 ms                                                | 6.36 ms: 1.01x faster                                                       |
| docutils       | 2.60 sec                                               | 2.48 sec: 1.05x faster                                                      |
| html5lib       | 63.2 ms                                                | 59.6 ms: 1.06x faster                                                       |
| tornado_http   | 96.6 ms                                                | 93.8 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230129-linux-x86_64-iritkatriel-stdlib_single_arg_ex-3.12.0a4+-23ae36b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 199 ms                                                 | 193 ms: 1.03x faster                                                        |
| float          | 76.3 ms                                                | 73.8 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230129-linux-x86_64-iritkatriel-stdlib_single_arg_ex-3.12.0a4+-23ae36b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 128 ms: 1.07x faster                                                        |
| regex_v8       | 22.3 ms                                                | 21.0 ms: 1.06x faster                                                       |
| regex_dna      | 203 ms                                                 | 202 ms: 1.01x faster                                                        |
| regex_effbot   | 3.36 ms                                                | 3.38 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230129-linux-x86_64-iritkatriel-stdlib_single_arg_ex-3.12.0a4+-23ae36b |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 12.7 ms                                                | 9.36 ms: 1.35x faster                                                       |
| unpickle_pure_python | 225 us                                                 | 199 us: 1.13x faster                                                        |
| json_loads           | 26.2 us                                                | 24.0 us: 1.09x faster                                                       |
| xml_etree_parse      | 158 ms                                                 | 147 ms: 1.08x faster                                                        |
| pickle_pure_python   | 304 us                                                 | 283 us: 1.07x faster                                                        |
| unpickle             | 13.3 us                                                | 13.0 us: 1.02x faster                                                       |
| pickle_dict          | 31.4 us                                                | 31.0 us: 1.01x faster                                                       |
| xml_etree_process    | 53.8 ms                                                | 53.2 ms: 1.01x faster                                                       |
| xml_etree_iterparse  | 103 ms                                                 | 102 ms: 1.00x faster                                                        |
| pickle_list          | 4.17 us                                                | 4.22 us: 1.01x slower                                                       |
| xml_etree_generate   | 76.2 ms                                                | 77.1 ms: 1.01x slower                                                       |
| pickle               | 9.79 us                                                | 10.2 us: 1.04x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                                |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230129-linux-x86_64-iritkatriel-stdlib_single_arg_ex-3.12.0a4+-23ae36b |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 8.36 ms                                                | 8.93 ms: 1.07x slower                                                       |
| python_startup_no_site | 5.96 ms                                                | 6.46 ms: 1.08x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.08x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230129-linux-x86_64-iritkatriel-stdlib_single_arg_ex-3.12.0a4+-23ae36b |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 52.1 ms                                                | 47.5 ms: 1.10x faster                                                       |
| genshi_text     | 22.1 ms                                                | 20.3 ms: 1.09x faster                                                       |
| django_template | 32.5 ms                                                | 32.3 ms: 1.00x faster                                                       |
| Geometric mean  | (ref)                                                  | 1.05x faster                                                                |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230129-linux-x86_64-iritkatriel-stdlib_single_arg_ex-3.12.0a4+-23ae36b |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps              | 12.7 ms                                                | 9.36 ms: 1.35x faster                                                       |
| deltablue               | 3.64 ms                                                | 3.20 ms: 1.14x faster                                                       |
| unpickle_pure_python    | 225 us                                                 | 199 us: 1.13x faster                                                        |
| richards                | 46.2 ms                                                | 41.9 ms: 1.10x faster                                                       |
| genshi_xml              | 52.1 ms                                                | 47.5 ms: 1.10x faster                                                       |
| logging_silent          | 98.5 ns                                                | 90.0 ns: 1.09x faster                                                       |
| json_loads              | 26.2 us                                                | 24.0 us: 1.09x faster                                                       |
| genshi_text             | 22.1 ms                                                | 20.3 ms: 1.09x faster                                                       |
| fannkuch                | 388 ms                                                 | 358 ms: 1.08x faster                                                        |
| hexiom                  | 6.35 ms                                                | 5.86 ms: 1.08x faster                                                       |
| scimark_sor             | 115 ms                                                 | 106 ms: 1.08x faster                                                        |
| scimark_sparse_mat_mult | 4.40 ms                                                | 4.06 ms: 1.08x faster                                                       |
| pycparser               | 1.17 sec                                               | 1.08 sec: 1.08x faster                                                      |
| json                    | 4.95 ms                                                | 4.58 ms: 1.08x faster                                                       |
| scimark_fft             | 329 ms                                                 | 305 ms: 1.08x faster                                                        |
| xml_etree_parse         | 158 ms                                                 | 147 ms: 1.08x faster                                                        |
| nqueens                 | 85.0 ms                                                | 79.1 ms: 1.07x faster                                                       |
| go                      | 143 ms                                                 | 133 ms: 1.07x faster                                                        |
| pickle_pure_python      | 304 us                                                 | 283 us: 1.07x faster                                                        |
| deepcopy_memo           | 36.4 us                                                | 34.1 us: 1.07x faster                                                       |
| sympy_str               | 287 ms                                                 | 269 ms: 1.07x faster                                                        |
| regex_compile           | 136 ms                                                 | 128 ms: 1.07x faster                                                        |
| sympy_sum               | 166 ms                                                 | 156 ms: 1.07x faster                                                        |
| bench_thread_pool       | 810 us                                                 | 761 us: 1.06x faster                                                        |
| chaos                   | 68.6 ms                                                | 64.5 ms: 1.06x faster                                                       |
| regex_v8                | 22.3 ms                                                | 21.0 ms: 1.06x faster                                                       |
| html5lib                | 63.2 ms                                                | 59.6 ms: 1.06x faster                                                       |
| logging_simple          | 6.06 us                                                | 5.72 us: 1.06x faster                                                       |
| spectral_norm           | 99.9 ms                                                | 94.4 ms: 1.06x faster                                                       |
| pprint_pformat          | 1.44 sec                                               | 1.36 sec: 1.06x faster                                                      |
| sympy_integrate         | 20.9 ms                                                | 19.7 ms: 1.06x faster                                                       |
| gunicorn                | 1.12 ms                                                | 1.06 ms: 1.06x faster                                                       |
| aiohttp                 | 1.05 ms                                                | 992 us: 1.05x faster                                                        |
| deepcopy                | 344 us                                                 | 327 us: 1.05x faster                                                        |
| logging_format          | 6.62 us                                                | 6.31 us: 1.05x faster                                                       |
| sympy_expand            | 472 ms                                                 | 451 ms: 1.05x faster                                                        |
| coroutines              | 26.1 ms                                                | 24.9 ms: 1.05x faster                                                       |
| docutils                | 2.60 sec                                               | 2.48 sec: 1.05x faster                                                      |
| sqlglot_optimize        | 53.0 ms                                                | 50.7 ms: 1.04x faster                                                       |
| telco                   | 6.62 ms                                                | 6.38 ms: 1.04x faster                                                       |
| raytrace                | 290 ms                                                 | 280 ms: 1.04x faster                                                        |
| pidigits                | 199 ms                                                 | 193 ms: 1.03x faster                                                        |
| float                   | 76.3 ms                                                | 73.8 ms: 1.03x faster                                                       |
| scimark_monte_carlo     | 68.3 ms                                                | 66.1 ms: 1.03x faster                                                       |
| tornado_http            | 96.6 ms                                                | 93.8 ms: 1.03x faster                                                       |
| pprint_safe_repr        | 691 ms                                                 | 670 ms: 1.03x faster                                                        |
| dulwich_log             | 63.9 ms                                                | 62.1 ms: 1.03x faster                                                       |
| pyflate                 | 417 ms                                                 | 406 ms: 1.03x faster                                                        |
| sqlglot_normalize       | 108 ms                                                 | 105 ms: 1.03x faster                                                        |
| async_generators        | 359 ms                                                 | 350 ms: 1.03x faster                                                        |
| 2to3                    | 257 ms                                                 | 251 ms: 1.02x faster                                                        |
| coverage                | 101 ms                                                 | 98.3 ms: 1.02x faster                                                       |
| unpack_sequence         | 43.4 ns                                                | 42.5 ns: 1.02x faster                                                       |
| mdp                     | 2.62 sec                                               | 2.57 sec: 1.02x faster                                                      |
| unpickle                | 13.3 us                                                | 13.0 us: 1.02x faster                                                       |
| pickle_dict             | 31.4 us                                                | 31.0 us: 1.01x faster                                                       |
| async_tree_none         | 529 ms                                                 | 522 ms: 1.01x faster                                                        |
| pathlib                 | 18.2 ms                                                | 18.0 ms: 1.01x faster                                                       |
| xml_etree_process       | 53.8 ms                                                | 53.2 ms: 1.01x faster                                                       |
| thrift                  | 752 us                                                 | 745 us: 1.01x faster                                                        |
| chameleon               | 6.41 ms                                                | 6.36 ms: 1.01x faster                                                       |
| meteor_contest          | 105 ms                                                 | 104 ms: 1.01x faster                                                        |
| regex_dna               | 203 ms                                                 | 202 ms: 1.01x faster                                                        |
| deepcopy_reduce         | 2.97 us                                                | 2.95 us: 1.01x faster                                                       |
| xml_etree_iterparse     | 103 ms                                                 | 102 ms: 1.00x faster                                                        |
| django_template         | 32.5 ms                                                | 32.3 ms: 1.00x faster                                                       |
| regex_effbot            | 3.36 ms                                                | 3.38 ms: 1.01x slower                                                       |
| pickle_list             | 4.17 us                                                | 4.22 us: 1.01x slower                                                       |
| xml_etree_generate      | 76.2 ms                                                | 77.1 ms: 1.01x slower                                                       |
| sqlglot_transpile       | 1.66 ms                                                | 1.69 ms: 1.02x slower                                                       |
| sqlglot_parse           | 1.37 ms                                                | 1.40 ms: 1.02x slower                                                       |
| pickle                  | 9.79 us                                                | 10.2 us: 1.04x slower                                                       |
| sqlite_synth            | 2.49 us                                                | 2.62 us: 1.05x slower                                                       |
| generators              | 72.2 ms                                                | 76.9 ms: 1.07x slower                                                       |
| python_startup          | 8.36 ms                                                | 8.93 ms: 1.07x slower                                                       |
| python_startup_no_site  | 5.96 ms                                                | 6.46 ms: 1.08x slower                                                       |
| mypy                    | 669 ms                                                 | 803 ms: 1.20x slower                                                        |
| Geometric mean          | (ref)                                                  | 1.03x faster                                                                |

Benchmark hidden because not significant (9): scimark_lu, unpickle_list, async_tree_io, bench_mp_pool, mako, crypto_pyaes, async_tree_cpu_io_mixed, nbody, async_tree_memoization
Ignored benchmarks (4) of /home/mdboom/Work/builds/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of /home/mdboom/Work/builds/benchmarking/results/bm-20230129-3.12.0a4+-23ae36b/bm-20230129-linux-x86_64-iritkatriel-stdlib_single_arg_ex-3.12.0a4+-23ae36b.json: asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal
