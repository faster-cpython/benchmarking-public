
# Results vs. 3.11.0

- fork: gvanrossum
- ref: e69c1f3e7a01d253e05b
- machine: linux-x86_64
- commit hash: e69c1f3
- commit date: 2023-01-26
- overall geometric mean: 1.04x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230126-linux-x86_64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4+-e69c1f3 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 250 ms: 1.04x faster                                                       |
| docutils       | 2.60 sec                                               | 2.50 sec: 1.04x faster                                                     |
| html5lib       | 64.8 ms                                                | 59.7 ms: 1.09x faster                                                      |
| tornado_http   | 96.5 ms                                                | 94.1 ms: 1.03x faster                                                      |
| Geometric mean | (ref)                                                  | 1.04x faster                                                               |

Benchmark hidden because not significant (1): chameleon

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230126-linux-x86_64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4+-e69c1f3 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 76.8 ms                                                | 71.8 ms: 1.07x faster                                                      |
| pidigits       | 197 ms                                                 | 193 ms: 1.02x faster                                                       |
| nbody          | 90.0 ms                                                | 95.4 ms: 1.06x slower                                                      |
| Geometric mean | (ref)                                                  | 1.01x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230126-linux-x86_64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4+-e69c1f3 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 127 ms: 1.07x faster                                                       |
| regex_v8       | 22.2 ms                                                | 21.2 ms: 1.05x faster                                                      |
| regex_dna      | 203 ms                                                 | 208 ms: 1.02x slower                                                       |
| regex_effbot   | 3.46 ms                                                | 3.54 ms: 1.03x slower                                                      |
| Geometric mean | (ref)                                                  | 1.02x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230126-linux-x86_64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4+-e69c1f3 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.40 ms: 1.31x faster                                                      |
| unpickle_pure_python | 227 us                                                 | 196 us: 1.16x faster                                                       |
| xml_etree_parse      | 160 ms                                                 | 147 ms: 1.09x faster                                                       |
| json_loads           | 26.1 us                                                | 24.0 us: 1.09x faster                                                      |
| pickle_pure_python   | 308 us                                                 | 286 us: 1.08x faster                                                       |
| pickle_list          | 4.14 us                                                | 3.96 us: 1.05x faster                                                      |
| pickle_dict          | 31.2 us                                                | 30.4 us: 1.02x faster                                                      |
| xml_etree_iterparse  | 104 ms                                                 | 103 ms: 1.01x faster                                                       |
| xml_etree_process    | 53.7 ms                                                | 54.0 ms: 1.01x slower                                                      |
| pickle               | 9.90 us                                                | 10.0 us: 1.01x slower                                                      |
| xml_etree_generate   | 75.9 ms                                                | 78.3 ms: 1.03x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                               |

Benchmark hidden because not significant (2): unpickle, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230126-linux-x86_64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4+-e69c1f3 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.90 ms: 1.04x slower                                                      |
| python_startup_no_site | 6.04 ms                                                | 6.44 ms: 1.07x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.05x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230126-linux-x86_64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4+-e69c1f3 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml      | 51.4 ms                                                | 47.3 ms: 1.09x faster                                                      |
| genshi_text     | 21.5 ms                                                | 21.2 ms: 1.02x faster                                                      |
| mako            | 9.83 ms                                                | 9.70 ms: 1.01x faster                                                      |
| django_template | 32.3 ms                                                | 32.5 ms: 1.01x slower                                                      |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                               |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230126-linux-x86_64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4+-e69c1f3 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_tcp             | 883 ms                                                 | 501 ms: 1.76x faster                                                       |
| json_dumps              | 12.4 ms                                                | 9.40 ms: 1.31x faster                                                      |
| scimark_sparse_mat_mult | 4.59 ms                                                | 3.95 ms: 1.16x faster                                                      |
| unpickle_pure_python    | 227 us                                                 | 196 us: 1.16x faster                                                       |
| deltablue               | 3.66 ms                                                | 3.22 ms: 1.13x faster                                                      |
| richards                | 46.1 ms                                                | 41.7 ms: 1.11x faster                                                      |
| xml_etree_parse         | 160 ms                                                 | 147 ms: 1.09x faster                                                       |
| json_loads              | 26.1 us                                                | 24.0 us: 1.09x faster                                                      |
| genshi_xml              | 51.4 ms                                                | 47.3 ms: 1.09x faster                                                      |
| html5lib                | 64.8 ms                                                | 59.7 ms: 1.09x faster                                                      |
| scimark_sor             | 115 ms                                                 | 106 ms: 1.08x faster                                                       |
| sympy_str               | 291 ms                                                 | 269 ms: 1.08x faster                                                       |
| pycparser               | 1.19 sec                                               | 1.10 sec: 1.08x faster                                                     |
| pickle_pure_python      | 308 us                                                 | 286 us: 1.08x faster                                                       |
| chaos                   | 68.7 ms                                                | 64.0 ms: 1.07x faster                                                      |
| regex_compile           | 136 ms                                                 | 127 ms: 1.07x faster                                                       |
| sympy_sum               | 166 ms                                                 | 155 ms: 1.07x faster                                                       |
| float                   | 76.8 ms                                                | 71.8 ms: 1.07x faster                                                      |
| nqueens                 | 83.8 ms                                                | 78.5 ms: 1.07x faster                                                      |
| pprint_pformat          | 1.46 sec                                               | 1.37 sec: 1.07x faster                                                     |
| sympy_integrate         | 21.0 ms                                                | 19.7 ms: 1.06x faster                                                      |
| unpack_sequence         | 44.5 ns                                                | 41.9 ns: 1.06x faster                                                      |
| hexiom                  | 6.34 ms                                                | 5.99 ms: 1.06x faster                                                      |
| logging_silent          | 98.0 ns                                                | 92.5 ns: 1.06x faster                                                      |
| pprint_safe_repr        | 706 ms                                                 | 667 ms: 1.06x faster                                                       |
| scimark_fft             | 325 ms                                                 | 308 ms: 1.06x faster                                                       |
| aiohttp                 | 1.05 ms                                                | 993 us: 1.06x faster                                                       |
| logging_simple          | 6.02 us                                                | 5.71 us: 1.05x faster                                                      |
| create_gc_cycles        | 1.52 ms                                                | 1.44 ms: 1.05x faster                                                      |
| sympy_expand            | 475 ms                                                 | 451 ms: 1.05x faster                                                       |
| json                    | 4.87 ms                                                | 4.63 ms: 1.05x faster                                                      |
| gc_traversal            | 3.82 ms                                                | 3.63 ms: 1.05x faster                                                      |
| crypto_pyaes            | 75.7 ms                                                | 72.1 ms: 1.05x faster                                                      |
| pyflate                 | 419 ms                                                 | 399 ms: 1.05x faster                                                       |
| gunicorn                | 1.12 ms                                                | 1.06 ms: 1.05x faster                                                      |
| fannkuch                | 384 ms                                                 | 367 ms: 1.05x faster                                                       |
| bench_thread_pool       | 817 us                                                 | 779 us: 1.05x faster                                                       |
| regex_v8                | 22.2 ms                                                | 21.2 ms: 1.05x faster                                                      |
| pickle_list             | 4.14 us                                                | 3.96 us: 1.05x faster                                                      |
| deepcopy_memo           | 35.8 us                                                | 34.3 us: 1.04x faster                                                      |
| deepcopy                | 341 us                                                 | 327 us: 1.04x faster                                                       |
| scimark_monte_carlo     | 68.0 ms                                                | 65.2 ms: 1.04x faster                                                      |
| docutils                | 2.60 sec                                               | 2.50 sec: 1.04x faster                                                     |
| sqlglot_optimize        | 52.7 ms                                                | 50.7 ms: 1.04x faster                                                      |
| coroutines              | 26.2 ms                                                | 25.2 ms: 1.04x faster                                                      |
| 2to3                    | 259 ms                                                 | 250 ms: 1.04x faster                                                       |
| sqlglot_normalize       | 108 ms                                                 | 104 ms: 1.04x faster                                                       |
| coverage                | 99.3 ms                                                | 96.1 ms: 1.03x faster                                                      |
| dulwich_log             | 64.0 ms                                                | 62.1 ms: 1.03x faster                                                      |
| mdp                     | 2.63 sec                                               | 2.55 sec: 1.03x faster                                                     |
| go                      | 140 ms                                                 | 136 ms: 1.03x faster                                                       |
| logging_format          | 6.48 us                                                | 6.31 us: 1.03x faster                                                      |
| tornado_http            | 96.5 ms                                                | 94.1 ms: 1.03x faster                                                      |
| raytrace                | 291 ms                                                 | 284 ms: 1.02x faster                                                       |
| pickle_dict             | 31.2 us                                                | 30.4 us: 1.02x faster                                                      |
| pidigits                | 197 ms                                                 | 193 ms: 1.02x faster                                                       |
| telco                   | 6.43 ms                                                | 6.30 ms: 1.02x faster                                                      |
| thrift                  | 760 us                                                 | 746 us: 1.02x faster                                                       |
| genshi_text             | 21.5 ms                                                | 21.2 ms: 1.02x faster                                                      |
| pathlib                 | 18.1 ms                                                | 17.8 ms: 1.02x faster                                                      |
| async_generators        | 356 ms                                                 | 351 ms: 1.01x faster                                                       |
| mako                    | 9.83 ms                                                | 9.70 ms: 1.01x faster                                                      |
| xml_etree_iterparse     | 104 ms                                                 | 103 ms: 1.01x faster                                                       |
| xml_etree_process       | 53.7 ms                                                | 54.0 ms: 1.01x slower                                                      |
| django_template         | 32.3 ms                                                | 32.5 ms: 1.01x slower                                                      |
| pickle                  | 9.90 us                                                | 10.0 us: 1.01x slower                                                      |
| regex_dna               | 203 ms                                                 | 208 ms: 1.02x slower                                                       |
| generators              | 73.5 ms                                                | 75.1 ms: 1.02x slower                                                      |
| regex_effbot            | 3.46 ms                                                | 3.54 ms: 1.03x slower                                                      |
| async_tree_cpu_io_mixed | 736 ms                                                 | 756 ms: 1.03x slower                                                       |
| xml_etree_generate      | 75.9 ms                                                | 78.3 ms: 1.03x slower                                                      |
| sqlglot_transpile       | 1.65 ms                                                | 1.70 ms: 1.03x slower                                                      |
| python_startup          | 8.58 ms                                                | 8.90 ms: 1.04x slower                                                      |
| sqlglot_parse           | 1.36 ms                                                | 1.42 ms: 1.04x slower                                                      |
| sqlite_synth            | 2.48 us                                                | 2.61 us: 1.05x slower                                                      |
| nbody                   | 90.0 ms                                                | 95.4 ms: 1.06x slower                                                      |
| python_startup_no_site  | 6.04 ms                                                | 6.44 ms: 1.07x slower                                                      |
| dask                    | 365 ms                                                 | 496 ms: 1.36x slower                                                       |
| Geometric mean          | (ref)                                                  | 1.04x faster                                                               |

Benchmark hidden because not significant (12): unpickle, async_tree_none, deepcopy_reduce, bench_mp_pool, chameleon, scimark_lu, async_tree_io, async_tree_memoization, meteor_contest, unpickle_list, djangocms, spectral_norm
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230126-3.12.0a4+-e69c1f3/bm-20230126-linux-x86_64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4+-e69c1f3.json: mypy
