
# Results vs. 3.11.0

- fork: iritkatriel
- ref: remove_JUMP_IF_FALSE
- machine: linux-x86_64
- commit hash: b2bf829
- commit date: 2023-03-22
- overall geometric mean: 1.04x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230322-linux-x86_64-iritkatriel-remove_JUMP_IF_FALSE-3.12.0a6+-b2bf829 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 248 ms: 1.05x faster                                                        |
| docutils       | 2.60 sec                                               | 2.53 sec: 1.03x faster                                                      |
| html5lib       | 64.8 ms                                                | 60.8 ms: 1.07x faster                                                       |
| tornado_http   | 96.5 ms                                                | 91.3 ms: 1.06x faster                                                       |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                |

Benchmark hidden because not significant (1): chameleon

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230322-linux-x86_64-iritkatriel-remove_JUMP_IF_FALSE-3.12.0a6+-b2bf829 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 197 ms                                                 | 189 ms: 1.04x faster                                                        |
| float          | 76.8 ms                                                | 74.1 ms: 1.04x faster                                                       |
| nbody          | 90.0 ms                                                | 87.1 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230322-linux-x86_64-iritkatriel-remove_JUMP_IF_FALSE-3.12.0a6+-b2bf829 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 133 ms: 1.03x faster                                                        |
| regex_v8       | 22.2 ms                                                | 21.8 ms: 1.02x faster                                                       |
| regex_effbot   | 3.46 ms                                                | 3.43 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230322-linux-x86_64-iritkatriel-remove_JUMP_IF_FALSE-3.12.0a6+-b2bf829 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.46 ms: 1.31x faster                                                       |
| unpickle_pure_python | 227 us                                                 | 198 us: 1.15x faster                                                        |
| json_loads           | 26.1 us                                                | 23.9 us: 1.09x faster                                                       |
| pickle_pure_python   | 308 us                                                 | 285 us: 1.08x faster                                                        |
| xml_etree_parse      | 160 ms                                                 | 153 ms: 1.05x faster                                                        |
| pickle_list          | 4.14 us                                                | 4.11 us: 1.01x faster                                                       |
| pickle_dict          | 31.2 us                                                | 31.9 us: 1.02x slower                                                       |
| pickle               | 9.90 us                                                | 10.2 us: 1.03x slower                                                       |
| unpickle             | 13.3 us                                                | 13.8 us: 1.04x slower                                                       |
| xml_etree_process    | 53.7 ms                                                | 56.1 ms: 1.05x slower                                                       |
| xml_etree_generate   | 75.9 ms                                                | 80.7 ms: 1.06x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                                |

Benchmark hidden because not significant (2): xml_etree_iterparse, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230322-linux-x86_64-iritkatriel-remove_JUMP_IF_FALSE-3.12.0a6+-b2bf829 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.81 ms: 1.03x slower                                                       |
| python_startup_no_site | 6.04 ms                                                | 6.51 ms: 1.08x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.05x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230322-linux-x86_64-iritkatriel-remove_JUMP_IF_FALSE-3.12.0a6+-b2bf829 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 51.4 ms                                                | 47.4 ms: 1.09x faster                                                       |
| genshi_text     | 21.5 ms                                                | 21.7 ms: 1.01x slower                                                       |
| mako            | 9.83 ms                                                | 9.94 ms: 1.01x slower                                                       |
| django_template | 32.3 ms                                                | 33.4 ms: 1.03x slower                                                       |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230322-linux-x86_64-iritkatriel-remove_JUMP_IF_FALSE-3.12.0a6+-b2bf829 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| generators              | 73.5 ms                                                | 29.0 ms: 2.53x faster                                                       |
| asyncio_tcp             | 883 ms                                                 | 506 ms: 1.75x faster                                                        |
| json_dumps              | 12.4 ms                                                | 9.46 ms: 1.31x faster                                                       |
| mypy2                   | 420 ms                                                 | 333 ms: 1.26x faster                                                        |
| coroutines              | 26.2 ms                                                | 22.3 ms: 1.17x faster                                                       |
| unpickle_pure_python    | 227 us                                                 | 198 us: 1.15x faster                                                        |
| deltablue               | 3.66 ms                                                | 3.21 ms: 1.14x faster                                                       |
| scimark_sparse_mat_mult | 4.59 ms                                                | 4.08 ms: 1.12x faster                                                       |
| scimark_fft             | 325 ms                                                 | 296 ms: 1.10x faster                                                        |
| spectral_norm           | 98.1 ms                                                | 89.6 ms: 1.10x faster                                                       |
| json_loads              | 26.1 us                                                | 23.9 us: 1.09x faster                                                       |
| scimark_sor             | 115 ms                                                 | 106 ms: 1.09x faster                                                        |
| genshi_xml              | 51.4 ms                                                | 47.4 ms: 1.09x faster                                                       |
| pickle_pure_python      | 308 us                                                 | 285 us: 1.08x faster                                                        |
| json                    | 4.87 ms                                                | 4.54 ms: 1.07x faster                                                       |
| html5lib                | 64.8 ms                                                | 60.8 ms: 1.07x faster                                                       |
| deepcopy_memo           | 35.8 us                                                | 33.7 us: 1.06x faster                                                       |
| unpack_sequence         | 44.5 ns                                                | 42.0 ns: 1.06x faster                                                       |
| tornado_http            | 96.5 ms                                                | 91.3 ms: 1.06x faster                                                       |
| pycparser               | 1.19 sec                                               | 1.12 sec: 1.06x faster                                                      |
| richards                | 46.1 ms                                                | 43.9 ms: 1.05x faster                                                       |
| scimark_monte_carlo     | 68.0 ms                                                | 64.7 ms: 1.05x faster                                                       |
| chaos                   | 68.7 ms                                                | 65.4 ms: 1.05x faster                                                       |
| xml_etree_parse         | 160 ms                                                 | 153 ms: 1.05x faster                                                        |
| deepcopy                | 341 us                                                 | 326 us: 1.05x faster                                                        |
| 2to3                    | 259 ms                                                 | 248 ms: 1.05x faster                                                        |
| go                      | 140 ms                                                 | 134 ms: 1.04x faster                                                        |
| pidigits                | 197 ms                                                 | 189 ms: 1.04x faster                                                        |
| aiohttp                 | 1.05 ms                                                | 1.01 ms: 1.04x faster                                                       |
| hexiom                  | 6.34 ms                                                | 6.11 ms: 1.04x faster                                                       |
| float                   | 76.8 ms                                                | 74.1 ms: 1.04x faster                                                       |
| sympy_expand            | 475 ms                                                 | 459 ms: 1.04x faster                                                        |
| nqueens                 | 83.8 ms                                                | 80.9 ms: 1.04x faster                                                       |
| coverage                | 99.3 ms                                                | 95.9 ms: 1.04x faster                                                       |
| deepcopy_reduce         | 3.02 us                                                | 2.92 us: 1.03x faster                                                       |
| bench_thread_pool       | 817 us                                                 | 790 us: 1.03x faster                                                        |
| fannkuch                | 384 ms                                                 | 372 ms: 1.03x faster                                                        |
| nbody                   | 90.0 ms                                                | 87.1 ms: 1.03x faster                                                       |
| mdp                     | 2.63 sec                                               | 2.55 sec: 1.03x faster                                                      |
| sympy_str               | 291 ms                                                 | 283 ms: 1.03x faster                                                        |
| docutils                | 2.60 sec                                               | 2.53 sec: 1.03x faster                                                      |
| pyflate                 | 419 ms                                                 | 407 ms: 1.03x faster                                                        |
| gunicorn                | 1.12 ms                                                | 1.09 ms: 1.03x faster                                                       |
| raytrace                | 291 ms                                                 | 284 ms: 1.03x faster                                                        |
| sqlalchemy_imperative   | 18.1 ms                                                | 17.6 ms: 1.03x faster                                                       |
| logging_simple          | 6.02 us                                                | 5.87 us: 1.03x faster                                                       |
| sqlglot_optimize        | 52.7 ms                                                | 51.4 ms: 1.03x faster                                                       |
| sympy_integrate         | 21.0 ms                                                | 20.4 ms: 1.03x faster                                                       |
| regex_compile           | 136 ms                                                 | 133 ms: 1.03x faster                                                        |
| sqlglot_normalize       | 108 ms                                                 | 105 ms: 1.02x faster                                                        |
| crypto_pyaes            | 75.7 ms                                                | 74.1 ms: 1.02x faster                                                       |
| regex_v8                | 22.2 ms                                                | 21.8 ms: 1.02x faster                                                       |
| pprint_pformat          | 1.46 sec                                               | 1.43 sec: 1.02x faster                                                      |
| create_gc_cycles        | 1.52 ms                                                | 1.49 ms: 1.02x faster                                                       |
| pprint_safe_repr        | 706 ms                                                 | 695 ms: 1.02x faster                                                        |
| logging_silent          | 98.0 ns                                                | 96.6 ns: 1.01x faster                                                       |
| pathlib                 | 18.1 ms                                                | 17.8 ms: 1.01x faster                                                       |
| logging_format          | 6.48 us                                                | 6.41 us: 1.01x faster                                                       |
| dulwich_log             | 64.0 ms                                                | 63.3 ms: 1.01x faster                                                       |
| meteor_contest          | 104 ms                                                 | 104 ms: 1.01x faster                                                        |
| regex_effbot            | 3.46 ms                                                | 3.43 ms: 1.01x faster                                                       |
| pickle_list             | 4.14 us                                                | 4.11 us: 1.01x faster                                                       |
| genshi_text             | 21.5 ms                                                | 21.7 ms: 1.01x slower                                                       |
| async_tree_cpu_io_mixed | 736 ms                                                 | 743 ms: 1.01x slower                                                        |
| mako                    | 9.83 ms                                                | 9.94 ms: 1.01x slower                                                       |
| pickle_dict             | 31.2 us                                                | 31.9 us: 1.02x slower                                                       |
| thrift                  | 760 us                                                 | 780 us: 1.03x slower                                                        |
| telco                   | 6.43 ms                                                | 6.60 ms: 1.03x slower                                                       |
| python_startup          | 8.58 ms                                                | 8.81 ms: 1.03x slower                                                       |
| pickle                  | 9.90 us                                                | 10.2 us: 1.03x slower                                                       |
| django_template         | 32.3 ms                                                | 33.4 ms: 1.03x slower                                                       |
| gc_traversal            | 3.82 ms                                                | 3.98 ms: 1.04x slower                                                       |
| unpickle                | 13.3 us                                                | 13.8 us: 1.04x slower                                                       |
| sqlite_synth            | 2.48 us                                                | 2.59 us: 1.04x slower                                                       |
| async_tree_memoization  | 624 ms                                                 | 653 ms: 1.05x slower                                                        |
| xml_etree_process       | 53.7 ms                                                | 56.1 ms: 1.05x slower                                                       |
| sqlglot_transpile       | 1.65 ms                                                | 1.75 ms: 1.06x slower                                                       |
| xml_etree_generate      | 75.9 ms                                                | 80.7 ms: 1.06x slower                                                       |
| sqlglot_parse           | 1.36 ms                                                | 1.45 ms: 1.07x slower                                                       |
| python_startup_no_site  | 6.04 ms                                                | 6.51 ms: 1.08x slower                                                       |
| async_generators        | 356 ms                                                 | 413 ms: 1.16x slower                                                        |
| dask                    | 365 ms                                                 | 503 ms: 1.38x slower                                                        |
| Geometric mean          | (ref)                                                  | 1.04x faster                                                                |

Benchmark hidden because not significant (11): djangocms, async_tree_none, xml_etree_iterparse, sympy_sum, async_tree_io, regex_dna, bench_mp_pool, unpickle_list, chameleon, scimark_lu, sqlalchemy_declarative
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, pylint
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230322-3.12.0a6+-b2bf829/bm-20230322-linux-x86_64-iritkatriel-remove_JUMP_IF_FALSE-3.12.0a6+-b2bf829.json: comprehensions
