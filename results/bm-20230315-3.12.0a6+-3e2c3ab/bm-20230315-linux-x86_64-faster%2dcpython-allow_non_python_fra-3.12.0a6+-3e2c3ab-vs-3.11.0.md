
# Results vs. 3.11.0

- fork: faster-cpython
- ref: allow_non_python_fra
- machine: linux-x86_64
- commit hash: 3e2c3ab
- commit date: 2023-03-15
- overall geometric mean: 1.03x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230315-linux-x86_64-faster%2dcpython-allow_non_python_fra-3.12.0a6+-3e2c3ab |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 252 ms: 1.03x faster                                                             |
| chameleon      | 6.38 ms                                                | 6.42 ms: 1.01x slower                                                            |
| docutils       | 2.60 sec                                               | 2.55 sec: 1.02x faster                                                           |
| html5lib       | 64.8 ms                                                | 62.1 ms: 1.04x faster                                                            |
| tornado_http   | 96.5 ms                                                | 95.2 ms: 1.01x faster                                                            |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230315-linux-x86_64-faster%2dcpython-allow_non_python_fra-3.12.0a6+-3e2c3ab |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 197 ms                                                 | 190 ms: 1.04x faster                                                             |
| float          | 76.8 ms                                                | 75.2 ms: 1.02x faster                                                            |
| nbody          | 90.0 ms                                                | 95.6 ms: 1.06x slower                                                            |
| Geometric mean | (ref)                                                  | 1.00x slower                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230315-linux-x86_64-faster%2dcpython-allow_non_python_fra-3.12.0a6+-3e2c3ab |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_effbot   | 3.46 ms                                                | 3.36 ms: 1.03x faster                                                            |
| regex_v8       | 22.2 ms                                                | 21.8 ms: 1.02x faster                                                            |
| regex_compile  | 136 ms                                                 | 134 ms: 1.02x faster                                                             |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                     |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230315-linux-x86_64-faster%2dcpython-allow_non_python_fra-3.12.0a6+-3e2c3ab |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.55 ms: 1.29x faster                                                            |
| unpickle_pure_python | 227 us                                                 | 201 us: 1.13x faster                                                             |
| xml_etree_parse      | 160 ms                                                 | 148 ms: 1.09x faster                                                             |
| pickle_pure_python   | 308 us                                                 | 286 us: 1.08x faster                                                             |
| json_loads           | 26.1 us                                                | 24.4 us: 1.07x faster                                                            |
| xml_etree_iterparse  | 104 ms                                                 | 99.4 ms: 1.05x faster                                                            |
| pickle_list          | 4.14 us                                                | 4.12 us: 1.01x faster                                                            |
| pickle_dict          | 31.2 us                                                | 31.1 us: 1.00x faster                                                            |
| unpickle_list        | 4.99 us                                                | 5.05 us: 1.01x slower                                                            |
| xml_etree_process    | 53.7 ms                                                | 55.2 ms: 1.03x slower                                                            |
| pickle               | 9.90 us                                                | 10.2 us: 1.03x slower                                                            |
| unpickle             | 13.3 us                                                | 13.8 us: 1.04x slower                                                            |
| xml_etree_generate   | 75.9 ms                                                | 81.0 ms: 1.07x slower                                                            |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230315-linux-x86_64-faster%2dcpython-allow_non_python_fra-3.12.0a6+-3e2c3ab |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 9.02 ms: 1.05x slower                                                            |
| python_startup_no_site | 6.04 ms                                                | 6.54 ms: 1.08x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230315-linux-x86_64-faster%2dcpython-allow_non_python_fra-3.12.0a6+-3e2c3ab |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_xml      | 51.4 ms                                                | 47.7 ms: 1.08x faster                                                            |
| mako            | 9.83 ms                                                | 10.0 ms: 1.02x slower                                                            |
| django_template | 32.3 ms                                                | 33.5 ms: 1.04x slower                                                            |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                                     |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230315-linux-x86_64-faster%2dcpython-allow_non_python_fra-3.12.0a6+-3e2c3ab |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| generators              | 73.5 ms                                                | 29.3 ms: 2.51x faster                                                            |
| asyncio_tcp             | 883 ms                                                 | 515 ms: 1.71x faster                                                             |
| json_dumps              | 12.4 ms                                                | 9.55 ms: 1.29x faster                                                            |
| mypy2                   | 420 ms                                                 | 335 ms: 1.25x faster                                                             |
| coroutines              | 26.2 ms                                                | 22.9 ms: 1.14x faster                                                            |
| deltablue               | 3.66 ms                                                | 3.21 ms: 1.14x faster                                                            |
| unpickle_pure_python    | 227 us                                                 | 201 us: 1.13x faster                                                             |
| xml_etree_parse         | 160 ms                                                 | 148 ms: 1.09x faster                                                             |
| scimark_sor             | 115 ms                                                 | 107 ms: 1.08x faster                                                             |
| genshi_xml              | 51.4 ms                                                | 47.7 ms: 1.08x faster                                                            |
| pickle_pure_python      | 308 us                                                 | 286 us: 1.08x faster                                                             |
| json_loads              | 26.1 us                                                | 24.4 us: 1.07x faster                                                            |
| coverage                | 99.3 ms                                                | 93.6 ms: 1.06x faster                                                            |
| json                    | 4.87 ms                                                | 4.64 ms: 1.05x faster                                                            |
| richards                | 46.1 ms                                                | 44.0 ms: 1.05x faster                                                            |
| pycparser               | 1.19 sec                                               | 1.13 sec: 1.05x faster                                                           |
| xml_etree_iterparse     | 104 ms                                                 | 99.4 ms: 1.05x faster                                                            |
| pprint_pformat          | 1.46 sec                                               | 1.39 sec: 1.04x faster                                                           |
| html5lib                | 64.8 ms                                                | 62.1 ms: 1.04x faster                                                            |
| deepcopy_memo           | 35.8 us                                                | 34.4 us: 1.04x faster                                                            |
| aiohttp                 | 1.05 ms                                                | 1.01 ms: 1.04x faster                                                            |
| pidigits                | 197 ms                                                 | 190 ms: 1.04x faster                                                             |
| sqlglot_optimize        | 52.7 ms                                                | 50.8 ms: 1.04x faster                                                            |
| fannkuch                | 384 ms                                                 | 371 ms: 1.04x faster                                                             |
| sqlglot_normalize       | 108 ms                                                 | 104 ms: 1.03x faster                                                             |
| pprint_safe_repr        | 706 ms                                                 | 683 ms: 1.03x faster                                                             |
| nqueens                 | 83.8 ms                                                | 81.1 ms: 1.03x faster                                                            |
| 2to3                    | 259 ms                                                 | 252 ms: 1.03x faster                                                             |
| bench_thread_pool       | 817 us                                                 | 793 us: 1.03x faster                                                             |
| sympy_expand            | 475 ms                                                 | 462 ms: 1.03x faster                                                             |
| regex_effbot            | 3.46 ms                                                | 3.36 ms: 1.03x faster                                                            |
| go                      | 140 ms                                                 | 137 ms: 1.03x faster                                                             |
| logging_simple          | 6.02 us                                                | 5.86 us: 1.03x faster                                                            |
| pyflate                 | 419 ms                                                 | 409 ms: 1.02x faster                                                             |
| float                   | 76.8 ms                                                | 75.2 ms: 1.02x faster                                                            |
| sympy_str               | 291 ms                                                 | 285 ms: 1.02x faster                                                             |
| docutils                | 2.60 sec                                               | 2.55 sec: 1.02x faster                                                           |
| sympy_integrate         | 21.0 ms                                                | 20.5 ms: 1.02x faster                                                            |
| deepcopy                | 341 us                                                 | 335 us: 1.02x faster                                                             |
| regex_v8                | 22.2 ms                                                | 21.8 ms: 1.02x faster                                                            |
| deepcopy_reduce         | 3.02 us                                                | 2.96 us: 1.02x faster                                                            |
| crypto_pyaes            | 75.7 ms                                                | 74.2 ms: 1.02x faster                                                            |
| logging_silent          | 98.0 ns                                                | 96.1 ns: 1.02x faster                                                            |
| scimark_fft             | 325 ms                                                 | 319 ms: 1.02x faster                                                             |
| gunicorn                | 1.12 ms                                                | 1.10 ms: 1.02x faster                                                            |
| regex_compile           | 136 ms                                                 | 134 ms: 1.02x faster                                                             |
| raytrace                | 291 ms                                                 | 287 ms: 1.02x faster                                                             |
| unpack_sequence         | 44.5 ns                                                | 43.8 ns: 1.02x faster                                                            |
| pathlib                 | 18.1 ms                                                | 17.8 ms: 1.01x faster                                                            |
| tornado_http            | 96.5 ms                                                | 95.2 ms: 1.01x faster                                                            |
| create_gc_cycles        | 1.52 ms                                                | 1.50 ms: 1.01x faster                                                            |
| chaos                   | 68.7 ms                                                | 67.9 ms: 1.01x faster                                                            |
| hexiom                  | 6.34 ms                                                | 6.27 ms: 1.01x faster                                                            |
| logging_format          | 6.48 us                                                | 6.41 us: 1.01x faster                                                            |
| pickle_list             | 4.14 us                                                | 4.12 us: 1.01x faster                                                            |
| meteor_contest          | 104 ms                                                 | 104 ms: 1.01x faster                                                             |
| dulwich_log             | 64.0 ms                                                | 63.8 ms: 1.00x faster                                                            |
| pickle_dict             | 31.2 us                                                | 31.1 us: 1.00x faster                                                            |
| chameleon               | 6.38 ms                                                | 6.42 ms: 1.01x slower                                                            |
| async_tree_cpu_io_mixed | 736 ms                                                 | 745 ms: 1.01x slower                                                             |
| unpickle_list           | 4.99 us                                                | 5.05 us: 1.01x slower                                                            |
| sympy_sum               | 166 ms                                                 | 168 ms: 1.01x slower                                                             |
| telco                   | 6.43 ms                                                | 6.52 ms: 1.01x slower                                                            |
| mako                    | 9.83 ms                                                | 10.0 ms: 1.02x slower                                                            |
| scimark_sparse_mat_mult | 4.59 ms                                                | 4.68 ms: 1.02x slower                                                            |
| gc_traversal            | 3.82 ms                                                | 3.93 ms: 1.03x slower                                                            |
| xml_etree_process       | 53.7 ms                                                | 55.2 ms: 1.03x slower                                                            |
| pickle                  | 9.90 us                                                | 10.2 us: 1.03x slower                                                            |
| django_template         | 32.3 ms                                                | 33.5 ms: 1.04x slower                                                            |
| scimark_lu              | 108 ms                                                 | 112 ms: 1.04x slower                                                             |
| unpickle                | 13.3 us                                                | 13.8 us: 1.04x slower                                                            |
| sqlglot_transpile       | 1.65 ms                                                | 1.72 ms: 1.04x slower                                                            |
| thrift                  | 760 us                                                 | 796 us: 1.05x slower                                                             |
| python_startup          | 8.58 ms                                                | 9.02 ms: 1.05x slower                                                            |
| sqlglot_parse           | 1.36 ms                                                | 1.44 ms: 1.06x slower                                                            |
| async_tree_memoization  | 624 ms                                                 | 660 ms: 1.06x slower                                                             |
| nbody                   | 90.0 ms                                                | 95.6 ms: 1.06x slower                                                            |
| xml_etree_generate      | 75.9 ms                                                | 81.0 ms: 1.07x slower                                                            |
| sqlite_synth            | 2.48 us                                                | 2.65 us: 1.07x slower                                                            |
| python_startup_no_site  | 6.04 ms                                                | 6.54 ms: 1.08x slower                                                            |
| async_generators        | 356 ms                                                 | 413 ms: 1.16x slower                                                             |
| dask                    | 365 ms                                                 | 509 ms: 1.39x slower                                                             |
| Geometric mean          | (ref)                                                  | 1.03x faster                                                                     |

Benchmark hidden because not significant (11): sqlalchemy_imperative, spectral_norm, sqlalchemy_declarative, genshi_text, scimark_monte_carlo, bench_mp_pool, async_tree_none, regex_dna, async_tree_io, mdp, djangocms
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, pylint
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230315-3.12.0a6+-3e2c3ab/bm-20230315-linux-x86_64-faster%2dcpython-allow_non_python_fra-3.12.0a6+-3e2c3ab.json: comprehensions
