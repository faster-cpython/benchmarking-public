
# Results vs. base

- fork: gvanrossum
- ref: e69c1f3e7a01d253e05b
- machine: darwin-arm64
- commit hash: e69c1f3
- commit date: 2023-01-26
- overall geometric mean: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230126-darwin-arm64-python-9f2c479eaf7d922746ef-3.12.0a4+-9f2c479 | bm-20230126-darwin-arm64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4+-e69c1f3 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 185 ms                                                                 | 181 ms: 1.02x faster                                                       |
| chameleon      | 4.52 ms                                                                | 4.58 ms: 1.01x slower                                                      |
| html5lib       | 35.1 ms                                                                | 34.9 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                               |

Benchmark hidden because not significant (2): docutils, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230126-darwin-arm64-python-9f2c479eaf7d922746ef-3.12.0a4+-9f2c479 | bm-20230126-darwin-arm64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4+-e69c1f3 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 51.8 ms                                                                | 52.4 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                               |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230126-darwin-arm64-python-9f2c479eaf7d922746ef-3.12.0a4+-9f2c479 | bm-20230126-darwin-arm64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4+-e69c1f3 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 73.7 ms                                                                | 73.6 ms: 1.00x faster                                                      |
| regex_dna      | 153 ms                                                                 | 150 ms: 1.02x faster                                                       |
| regex_effbot   | 2.60 ms                                                                | 2.61 ms: 1.00x slower                                                      |
| regex_v8       | 16.1 ms                                                                | 16.1 ms: 1.00x faster                                                      |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230126-darwin-arm64-python-9f2c479eaf7d922746ef-3.12.0a4+-9f2c479 | bm-20230126-darwin-arm64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4+-e69c1f3 |
|----------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 6.23 ms                                                                | 6.15 ms: 1.01x faster                                                      |
| pickle_pure_python   | 194 us                                                                 | 194 us: 1.00x slower                                                       |
| unpickle_list        | 2.77 us                                                                | 2.71 us: 1.02x faster                                                      |
| unpickle_pure_python | 147 us                                                                 | 145 us: 1.01x faster                                                       |
| xml_etree_parse      | 93.7 ms                                                                | 94.8 ms: 1.01x slower                                                      |
| xml_etree_iterparse  | 67.7 ms                                                                | 68.3 ms: 1.01x slower                                                      |
| xml_etree_process    | 35.6 ms                                                                | 35.4 ms: 1.01x faster                                                      |
| Geometric mean       | (ref)                                                                  | 1.00x faster                                                               |

Benchmark hidden because not significant (6): json_loads, pickle, pickle_dict, pickle_list, unpickle, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230126-darwin-arm64-python-9f2c479eaf7d922746ef-3.12.0a4+-9f2c479 | bm-20230126-darwin-arm64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4+-e69c1f3 |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 7.39 ms                                                                | 7.38 ms: 1.00x faster                                                      |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                               |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20230126-darwin-arm64-python-9f2c479eaf7d922746ef-3.12.0a4+-9f2c479 | bm-20230126-darwin-arm64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4+-e69c1f3 |
|-----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 21.3 ms                                                                | 21.1 ms: 1.01x faster                                                      |
| genshi_text     | 14.7 ms                                                                | 14.8 ms: 1.01x slower                                                      |
| mako            | 7.27 ms                                                                | 7.29 ms: 1.00x slower                                                      |
| Geometric mean  | (ref)                                                                  | 1.00x slower                                                               |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark               | bm-20230126-darwin-arm64-python-9f2c479eaf7d922746ef-3.12.0a4+-9f2c479 | bm-20230126-darwin-arm64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4+-e69c1f3 |
|-------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3                    | 185 ms                                                                 | 181 ms: 1.02x faster                                                       |
| async_generators        | 199 ms                                                                 | 200 ms: 1.00x slower                                                       |
| async_tree_memoization  | 324 ms                                                                 | 332 ms: 1.02x slower                                                       |
| asyncio_tcp             | 446 ms                                                                 | 395 ms: 1.13x faster                                                       |
| chameleon               | 4.52 ms                                                                | 4.58 ms: 1.01x slower                                                      |
| chaos                   | 47.8 ms                                                                | 48.1 ms: 1.01x slower                                                      |
| bench_thread_pool       | 450 us                                                                 | 447 us: 1.01x faster                                                       |
| coroutines              | 18.8 ms                                                                | 18.6 ms: 1.01x faster                                                      |
| coverage                | 56.9 ms                                                                | 57.4 ms: 1.01x slower                                                      |
| crypto_pyaes            | 51.9 ms                                                                | 52.1 ms: 1.00x slower                                                      |
| deepcopy                | 219 us                                                                 | 220 us: 1.00x slower                                                       |
| deepcopy_memo           | 26.0 us                                                                | 26.1 us: 1.00x slower                                                      |
| deltablue               | 2.50 ms                                                                | 2.59 ms: 1.04x slower                                                      |
| django_template         | 21.3 ms                                                                | 21.1 ms: 1.01x faster                                                      |
| fannkuch                | 256 ms                                                                 | 255 ms: 1.00x faster                                                       |
| float                   | 51.8 ms                                                                | 52.4 ms: 1.01x slower                                                      |
| create_gc_cycles        | 692 us                                                                 | 711 us: 1.03x slower                                                       |
| gc_traversal            | 2.41 ms                                                                | 2.43 ms: 1.01x slower                                                      |
| generators              | 34.6 ms                                                                | 34.4 ms: 1.01x faster                                                      |
| genshi_text             | 14.7 ms                                                                | 14.8 ms: 1.01x slower                                                      |
| go                      | 110 ms                                                                 | 109 ms: 1.01x faster                                                       |
| hexiom                  | 4.73 ms                                                                | 4.71 ms: 1.01x faster                                                      |
| html5lib                | 35.1 ms                                                                | 34.9 ms: 1.01x faster                                                      |
| json_dumps              | 6.23 ms                                                                | 6.15 ms: 1.01x faster                                                      |
| logging_format          | 3.80 us                                                                | 3.87 us: 1.02x slower                                                      |
| logging_silent          | 66.3 ns                                                                | 66.0 ns: 1.00x faster                                                      |
| logging_simple          | 3.53 us                                                                | 3.60 us: 1.02x slower                                                      |
| mako                    | 7.27 ms                                                                | 7.29 ms: 1.00x slower                                                      |
| mdp                     | 1.51 sec                                                               | 1.52 sec: 1.00x slower                                                     |
| meteor_contest          | 73.8 ms                                                                | 73.0 ms: 1.01x faster                                                      |
| pickle_pure_python      | 194 us                                                                 | 194 us: 1.00x slower                                                       |
| pprint_safe_repr        | 465 ms                                                                 | 462 ms: 1.01x faster                                                       |
| pprint_pformat          | 946 ms                                                                 | 941 ms: 1.01x faster                                                       |
| pyflate                 | 324 ms                                                                 | 322 ms: 1.01x faster                                                       |
| python_startup_no_site  | 7.39 ms                                                                | 7.38 ms: 1.00x faster                                                      |
| raytrace                | 216 ms                                                                 | 210 ms: 1.03x faster                                                       |
| regex_compile           | 73.7 ms                                                                | 73.6 ms: 1.00x faster                                                      |
| regex_dna               | 153 ms                                                                 | 150 ms: 1.02x faster                                                       |
| regex_effbot            | 2.60 ms                                                                | 2.61 ms: 1.00x slower                                                      |
| regex_v8                | 16.1 ms                                                                | 16.1 ms: 1.00x faster                                                      |
| richards                | 31.1 ms                                                                | 30.7 ms: 1.01x faster                                                      |
| scimark_fft             | 193 ms                                                                 | 193 ms: 1.00x faster                                                       |
| scimark_lu              | 71.0 ms                                                                | 71.5 ms: 1.01x slower                                                      |
| scimark_monte_carlo     | 50.4 ms                                                                | 45.7 ms: 1.10x faster                                                      |
| scimark_sor             | 78.3 ms                                                                | 85.2 ms: 1.09x slower                                                      |
| scimark_sparse_mat_mult | 2.82 ms                                                                | 2.83 ms: 1.00x slower                                                      |
| spectral_norm           | 72.3 ms                                                                | 72.8 ms: 1.01x slower                                                      |
| sqlglot_optimize        | 31.4 ms                                                                | 31.7 ms: 1.01x slower                                                      |
| sqlglot_normalize       | 172 ms                                                                 | 174 ms: 1.01x slower                                                       |
| sqlite_synth            | 1.36 us                                                                | 1.36 us: 1.01x slower                                                      |
| sympy_expand            | 240 ms                                                                 | 241 ms: 1.00x slower                                                       |
| sympy_integrate         | 11.1 ms                                                                | 11.2 ms: 1.00x slower                                                      |
| sympy_sum               | 81.4 ms                                                                | 82.0 ms: 1.01x slower                                                      |
| thrift                  | 443 us                                                                 | 444 us: 1.00x slower                                                       |
| unpack_sequence         | 32.7 ns                                                                | 33.6 ns: 1.03x slower                                                      |
| unpickle_list           | 2.77 us                                                                | 2.71 us: 1.02x faster                                                      |
| unpickle_pure_python    | 147 us                                                                 | 145 us: 1.01x faster                                                       |
| xml_etree_parse         | 93.7 ms                                                                | 94.8 ms: 1.01x slower                                                      |
| xml_etree_iterparse     | 67.7 ms                                                                | 68.3 ms: 1.01x slower                                                      |
| xml_etree_process       | 35.6 ms                                                                | 35.4 ms: 1.01x faster                                                      |
| Geometric mean          | (ref)                                                                  | 1.00x faster                                                               |

Benchmark hidden because not significant (28): async_tree_none, async_tree_cpu_io_mixed, async_tree_io, bench_mp_pool, dask, deepcopy_reduce, docutils, dulwich_log, genshi_xml, json, json_loads, mypy, nbody, nqueens, pathlib, pickle, pickle_dict, pickle_list, pidigits, pycparser, python_startup, sqlglot_parse, sqlglot_transpile, sympy_str, telco, tornado_http, unpickle, xml_etree_generate
