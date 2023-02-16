
# Results vs. 3.11.0

- fork: python
- ref: b724ac2fe7fbb5a7a33d
- machine: linux-x86_64
- commit hash: b724ac2
- commit date: 2023-01-23
- overall geometric mean: 1.03x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230123-linux-x86_64-python-b724ac2fe7fbb5a7a33d-3.12.0a4+-b724ac2 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 253 ms: 1.03x faster                                                   |
| chameleon      | 6.38 ms                                                | 6.42 ms: 1.01x slower                                                  |
| docutils       | 2.60 sec                                               | 2.52 sec: 1.03x faster                                                 |
| html5lib       | 64.8 ms                                                | 60.3 ms: 1.07x faster                                                  |
| tornado_http   | 96.5 ms                                                | 93.7 ms: 1.03x faster                                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230123-linux-x86_64-python-b724ac2fe7fbb5a7a33d-3.12.0a4+-b724ac2 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 76.8 ms                                                | 72.6 ms: 1.06x faster                                                  |
| pidigits       | 197 ms                                                 | 197 ms: 1.00x slower                                                   |
| nbody          | 90.0 ms                                                | 93.8 ms: 1.04x slower                                                  |
| Geometric mean | (ref)                                                  | 1.00x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230123-linux-x86_64-python-b724ac2fe7fbb5a7a33d-3.12.0a4+-b724ac2 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_v8       | 22.2 ms                                                | 21.0 ms: 1.06x faster                                                  |
| regex_compile  | 136 ms                                                 | 129 ms: 1.06x faster                                                   |
| regex_dna      | 203 ms                                                 | 201 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                  | 1.03x faster                                                           |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230123-linux-x86_64-python-b724ac2fe7fbb5a7a33d-3.12.0a4+-b724ac2 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.38 ms: 1.32x faster                                                  |
| unpickle_pure_python | 227 us                                                 | 197 us: 1.15x faster                                                   |
| pickle_pure_python   | 308 us                                                 | 284 us: 1.08x faster                                                   |
| json_loads           | 26.1 us                                                | 24.3 us: 1.07x faster                                                  |
| xml_etree_parse      | 160 ms                                                 | 156 ms: 1.03x faster                                                   |
| xml_etree_process    | 53.7 ms                                                | 54.4 ms: 1.01x slower                                                  |
| unpickle_list        | 4.99 us                                                | 5.08 us: 1.02x slower                                                  |
| xml_etree_iterparse  | 104 ms                                                 | 106 ms: 1.02x slower                                                   |
| pickle_list          | 4.14 us                                                | 4.26 us: 1.03x slower                                                  |
| pickle_dict          | 31.2 us                                                | 32.2 us: 1.03x slower                                                  |
| xml_etree_generate   | 75.9 ms                                                | 79.1 ms: 1.04x slower                                                  |
| pickle               | 9.90 us                                                | 10.3 us: 1.04x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                           |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230123-linux-x86_64-python-b724ac2fe7fbb5a7a33d-3.12.0a4+-b724ac2 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.96 ms: 1.04x slower                                                  |
| python_startup_no_site | 6.04 ms                                                | 6.49 ms: 1.08x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230123-linux-x86_64-python-b724ac2fe7fbb5a7a33d-3.12.0a4+-b724ac2 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_xml      | 51.4 ms                                                | 46.8 ms: 1.10x faster                                                  |
| mako            | 9.83 ms                                                | 9.66 ms: 1.02x faster                                                  |
| django_template | 32.3 ms                                                | 32.9 ms: 1.02x slower                                                  |
| genshi_text     | 21.5 ms                                                | 22.1 ms: 1.03x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230123-linux-x86_64-python-b724ac2fe7fbb5a7a33d-3.12.0a4+-b724ac2 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| asyncio_tcp             | 883 ms                                                 | 490 ms: 1.80x faster                                                   |
| json_dumps              | 12.4 ms                                                | 9.38 ms: 1.32x faster                                                  |
| unpickle_pure_python    | 227 us                                                 | 197 us: 1.15x faster                                                   |
| scimark_sparse_mat_mult | 4.59 ms                                                | 4.06 ms: 1.13x faster                                                  |
| deltablue               | 3.66 ms                                                | 3.23 ms: 1.13x faster                                                  |
| nqueens                 | 83.8 ms                                                | 76.2 ms: 1.10x faster                                                  |
| genshi_xml              | 51.4 ms                                                | 46.8 ms: 1.10x faster                                                  |
| scimark_sor             | 115 ms                                                 | 105 ms: 1.09x faster                                                   |
| pickle_pure_python      | 308 us                                                 | 284 us: 1.08x faster                                                   |
| pycparser               | 1.19 sec                                               | 1.10 sec: 1.08x faster                                                 |
| mdp                     | 2.63 sec                                               | 2.43 sec: 1.08x faster                                                 |
| chaos                   | 68.7 ms                                                | 63.6 ms: 1.08x faster                                                  |
| richards                | 46.1 ms                                                | 42.9 ms: 1.07x faster                                                  |
| html5lib                | 64.8 ms                                                | 60.3 ms: 1.07x faster                                                  |
| json_loads              | 26.1 us                                                | 24.3 us: 1.07x faster                                                  |
| unpack_sequence         | 44.5 ns                                                | 41.6 ns: 1.07x faster                                                  |
| hexiom                  | 6.34 ms                                                | 5.95 ms: 1.06x faster                                                  |
| scimark_fft             | 325 ms                                                 | 306 ms: 1.06x faster                                                   |
| fannkuch                | 384 ms                                                 | 363 ms: 1.06x faster                                                   |
| regex_v8                | 22.2 ms                                                | 21.0 ms: 1.06x faster                                                  |
| float                   | 76.8 ms                                                | 72.6 ms: 1.06x faster                                                  |
| json                    | 4.87 ms                                                | 4.60 ms: 1.06x faster                                                  |
| aiohttp                 | 1.05 ms                                                | 994 us: 1.06x faster                                                   |
| regex_compile           | 136 ms                                                 | 129 ms: 1.06x faster                                                   |
| bench_thread_pool       | 817 us                                                 | 774 us: 1.05x faster                                                   |
| logging_silent          | 98.0 ns                                                | 93.3 ns: 1.05x faster                                                  |
| pprint_pformat          | 1.46 sec                                               | 1.39 sec: 1.05x faster                                                 |
| logging_simple          | 6.02 us                                                | 5.74 us: 1.05x faster                                                  |
| pyflate                 | 419 ms                                                 | 400 ms: 1.05x faster                                                   |
| pprint_safe_repr        | 706 ms                                                 | 674 ms: 1.05x faster                                                   |
| gunicorn                | 1.12 ms                                                | 1.07 ms: 1.04x faster                                                  |
| deepcopy                | 341 us                                                 | 327 us: 1.04x faster                                                   |
| sympy_expand            | 475 ms                                                 | 456 ms: 1.04x faster                                                   |
| scimark_monte_carlo     | 68.0 ms                                                | 65.2 ms: 1.04x faster                                                  |
| raytrace                | 291 ms                                                 | 280 ms: 1.04x faster                                                   |
| sympy_str               | 291 ms                                                 | 281 ms: 1.04x faster                                                   |
| sympy_integrate         | 21.0 ms                                                | 20.2 ms: 1.03x faster                                                  |
| deepcopy_memo           | 35.8 us                                                | 34.6 us: 1.03x faster                                                  |
| docutils                | 2.60 sec                                               | 2.52 sec: 1.03x faster                                                 |
| go                      | 140 ms                                                 | 136 ms: 1.03x faster                                                   |
| crypto_pyaes            | 75.7 ms                                                | 73.3 ms: 1.03x faster                                                  |
| dulwich_log             | 64.0 ms                                                | 62.0 ms: 1.03x faster                                                  |
| djangocms               | 32.5 us                                                | 31.6 us: 1.03x faster                                                  |
| tornado_http            | 96.5 ms                                                | 93.7 ms: 1.03x faster                                                  |
| sqlglot_normalize       | 108 ms                                                 | 105 ms: 1.03x faster                                                   |
| sqlglot_optimize        | 52.7 ms                                                | 51.3 ms: 1.03x faster                                                  |
| xml_etree_parse         | 160 ms                                                 | 156 ms: 1.03x faster                                                   |
| 2to3                    | 259 ms                                                 | 253 ms: 1.03x faster                                                   |
| coroutines              | 26.2 ms                                                | 25.6 ms: 1.02x faster                                                  |
| logging_format          | 6.48 us                                                | 6.34 us: 1.02x faster                                                  |
| create_gc_cycles        | 1.52 ms                                                | 1.48 ms: 1.02x faster                                                  |
| coverage                | 99.3 ms                                                | 97.3 ms: 1.02x faster                                                  |
| thrift                  | 760 us                                                 | 746 us: 1.02x faster                                                   |
| mako                    | 9.83 ms                                                | 9.66 ms: 1.02x faster                                                  |
| deepcopy_reduce         | 3.02 us                                                | 2.97 us: 1.02x faster                                                  |
| sympy_sum               | 166 ms                                                 | 164 ms: 1.01x faster                                                   |
| async_generators        | 356 ms                                                 | 351 ms: 1.01x faster                                                   |
| pathlib                 | 18.1 ms                                                | 17.9 ms: 1.01x faster                                                  |
| regex_dna               | 203 ms                                                 | 201 ms: 1.01x faster                                                   |
| telco                   | 6.43 ms                                                | 6.38 ms: 1.01x faster                                                  |
| scimark_lu              | 108 ms                                                 | 107 ms: 1.01x faster                                                   |
| pidigits                | 197 ms                                                 | 197 ms: 1.00x slower                                                   |
| chameleon               | 6.38 ms                                                | 6.42 ms: 1.01x slower                                                  |
| xml_etree_process       | 53.7 ms                                                | 54.4 ms: 1.01x slower                                                  |
| generators              | 73.5 ms                                                | 74.7 ms: 1.02x slower                                                  |
| unpickle_list           | 4.99 us                                                | 5.08 us: 1.02x slower                                                  |
| django_template         | 32.3 ms                                                | 32.9 ms: 1.02x slower                                                  |
| async_tree_io           | 1.30 sec                                               | 1.33 sec: 1.02x slower                                                 |
| xml_etree_iterparse     | 104 ms                                                 | 106 ms: 1.02x slower                                                   |
| genshi_text             | 21.5 ms                                                | 22.1 ms: 1.03x slower                                                  |
| async_tree_cpu_io_mixed | 736 ms                                                 | 755 ms: 1.03x slower                                                   |
| pickle_list             | 4.14 us                                                | 4.26 us: 1.03x slower                                                  |
| pickle_dict             | 31.2 us                                                | 32.2 us: 1.03x slower                                                  |
| sqlglot_transpile       | 1.65 ms                                                | 1.71 ms: 1.04x slower                                                  |
| gc_traversal            | 3.82 ms                                                | 3.96 ms: 1.04x slower                                                  |
| sqlglot_parse           | 1.36 ms                                                | 1.41 ms: 1.04x slower                                                  |
| sqlite_synth            | 2.48 us                                                | 2.58 us: 1.04x slower                                                  |
| nbody                   | 90.0 ms                                                | 93.8 ms: 1.04x slower                                                  |
| xml_etree_generate      | 75.9 ms                                                | 79.1 ms: 1.04x slower                                                  |
| pickle                  | 9.90 us                                                | 10.3 us: 1.04x slower                                                  |
| python_startup          | 8.58 ms                                                | 8.96 ms: 1.04x slower                                                  |
| async_tree_memoization  | 624 ms                                                 | 666 ms: 1.07x slower                                                   |
| python_startup_no_site  | 6.04 ms                                                | 6.49 ms: 1.08x slower                                                  |
| dask                    | 365 ms                                                 | 495 ms: 1.36x slower                                                   |
| Geometric mean          | (ref)                                                  | 1.03x faster                                                           |

Benchmark hidden because not significant (6): spectral_norm, regex_effbot, bench_mp_pool, meteor_contest, async_tree_none, unpickle
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230123-3.12.0a4+-b724ac2/bm-20230123-linux-x86_64-python-b724ac2fe7fbb5a7a33d-3.12.0a4+-b724ac2.json: mypy
