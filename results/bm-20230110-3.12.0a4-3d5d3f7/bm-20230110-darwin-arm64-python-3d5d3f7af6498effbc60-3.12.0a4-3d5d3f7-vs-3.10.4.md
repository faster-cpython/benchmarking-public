
# Results vs. 3.10.4

- fork: python
- ref: 3d5d3f7af6498effbc60
- machine: darwin-arm64
- commit hash: 3d5d3f7
- commit date: 2023-01-10
- overall geometric mean: 1.22x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.17x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230110-darwin-arm64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 202 ms                                                 | 163 ms: 1.25x faster                                                  |
| chameleon      | 5.84 ms                                                | 4.53 ms: 1.29x faster                                                 |
| docutils       | 1.78 sec                                               | 1.45 sec: 1.23x faster                                                |
| html5lib       | 44.1 ms                                                | 35.0 ms: 1.26x faster                                                 |
| Geometric mean | (ref)                                                  | 1.26x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230110-darwin-arm64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 94.1 ms                                                | 63.9 ms: 1.47x faster                                                 |
| float          | 72.3 ms                                                | 52.0 ms: 1.39x faster                                                 |
| pidigits       | 282 ms                                                 | 281 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.27x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230110-darwin-arm64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 96.6 ms                                                | 74.5 ms: 1.30x faster                                                 |
| regex_v8       | 17.5 ms                                                | 15.7 ms: 1.12x faster                                                 |
| regex_dna      | 160 ms                                                 | 149 ms: 1.07x faster                                                  |
| regex_effbot   | 2.45 ms                                                | 2.61 ms: 1.07x slower                                                 |
| Geometric mean | (ref)                                                  | 1.10x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230110-darwin-arm64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 284 us                                                 | 192 us: 1.47x faster                                                  |
| unpickle_pure_python | 203 us                                                 | 143 us: 1.43x faster                                                  |
| json_dumps           | 8.38 ms                                                | 6.05 ms: 1.39x faster                                                 |
| xml_etree_process    | 45.1 ms                                                | 34.9 ms: 1.29x faster                                                 |
| xml_etree_generate   | 54.3 ms                                                | 48.6 ms: 1.12x faster                                                 |
| xml_etree_parse      | 107 ms                                                 | 96.5 ms: 1.11x faster                                                 |
| xml_etree_iterparse  | 72.6 ms                                                | 69.4 ms: 1.05x faster                                                 |
| json_loads           | 16.9 us                                                | 16.2 us: 1.04x faster                                                 |
| pickle_dict          | 17.8 us                                                | 18.0 us: 1.01x slower                                                 |
| pickle               | 7.36 us                                                | 7.44 us: 1.01x slower                                                 |
| unpickle_list        | 2.66 us                                                | 2.70 us: 1.01x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.13x faster                                                          |

Benchmark hidden because not significant (2): unpickle, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230110-darwin-arm64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 12.6 ms                                                | 12.3 ms: 1.03x faster                                                 |
| python_startup_no_site | 9.73 ms                                                | 10.2 ms: 1.05x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230110-darwin-arm64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_xml      | 37.6 ms                                                | 28.4 ms: 1.32x faster                                                 |
| mako            | 10.5 ms                                                | 8.12 ms: 1.29x faster                                                 |
| django_template | 27.3 ms                                                | 21.6 ms: 1.26x faster                                                 |
| genshi_text     | 18.4 ms                                                | 15.2 ms: 1.21x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.27x faster                                                          |

All benchmarks:
===============

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230110-darwin-arm64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deltablue               | 5.15 ms                                                | 2.64 ms: 1.95x faster                                                 |
| logging_silent          | 119 ns                                                 | 66.4 ns: 1.79x faster                                                 |
| richards                | 51.4 ms                                                | 30.6 ms: 1.68x faster                                                 |
| scimark_sor             | 127 ms                                                 | 82.8 ms: 1.53x faster                                                 |
| go                      | 165 ms                                                 | 109 ms: 1.51x faster                                                  |
| scimark_lu              | 110 ms                                                 | 72.7 ms: 1.51x faster                                                 |
| raytrace                | 328 ms                                                 | 217 ms: 1.51x faster                                                  |
| asyncio_tcp             | 673 ms                                                 | 449 ms: 1.50x faster                                                  |
| async_tree_memoization  | 493 ms                                                 | 332 ms: 1.49x faster                                                  |
| crypto_pyaes            | 78.0 ms                                                | 52.6 ms: 1.48x faster                                                 |
| nbody                   | 94.1 ms                                                | 63.9 ms: 1.47x faster                                                 |
| pickle_pure_python      | 284 us                                                 | 192 us: 1.47x faster                                                  |
| scimark_monte_carlo     | 72.2 ms                                                | 49.6 ms: 1.46x faster                                                 |
| unpickle_pure_python    | 203 us                                                 | 143 us: 1.43x faster                                                  |
| pyflate                 | 453 ms                                                 | 318 ms: 1.42x faster                                                  |
| async_tree_none         | 402 ms                                                 | 288 ms: 1.40x faster                                                  |
| float                   | 72.3 ms                                                | 52.0 ms: 1.39x faster                                                 |
| json_dumps              | 8.38 ms                                                | 6.05 ms: 1.39x faster                                                 |
| async_tree_io           | 1.02 sec                                               | 748 ms: 1.36x faster                                                  |
| pycparser               | 915 ms                                                 | 676 ms: 1.35x faster                                                  |
| logging_simple          | 4.63 us                                                | 3.44 us: 1.35x faster                                                 |
| logging_format          | 5.01 us                                                | 3.74 us: 1.34x faster                                                 |
| thrift                  | 586 us                                                 | 438 us: 1.34x faster                                                  |
| genshi_xml              | 37.6 ms                                                | 28.4 ms: 1.32x faster                                                 |
| chaos                   | 66.8 ms                                                | 50.5 ms: 1.32x faster                                                 |
| pprint_pformat          | 1.24 sec                                               | 939 ms: 1.32x faster                                                  |
| pprint_safe_repr        | 609 ms                                                 | 462 ms: 1.32x faster                                                  |
| deepcopy_memo           | 34.5 us                                                | 26.2 us: 1.32x faster                                                 |
| spectral_norm           | 96.4 ms                                                | 73.4 ms: 1.31x faster                                                 |
| regex_compile           | 96.6 ms                                                | 74.5 ms: 1.30x faster                                                 |
| xml_etree_process       | 45.1 ms                                                | 34.9 ms: 1.29x faster                                                 |
| mako                    | 10.5 ms                                                | 8.12 ms: 1.29x faster                                                 |
| chameleon               | 5.84 ms                                                | 4.53 ms: 1.29x faster                                                 |
| sqlglot_parse           | 1.33 ms                                                | 1.04 ms: 1.29x faster                                                 |
| sqlglot_transpile       | 1.54 ms                                                | 1.20 ms: 1.28x faster                                                 |
| hexiom                  | 6.32 ms                                                | 4.94 ms: 1.28x faster                                                 |
| create_gc_cycles        | 876 us                                                 | 692 us: 1.27x faster                                                  |
| django_template         | 27.3 ms                                                | 21.6 ms: 1.26x faster                                                 |
| html5lib                | 44.1 ms                                                | 35.0 ms: 1.26x faster                                                 |
| deepcopy                | 278 us                                                 | 221 us: 1.26x faster                                                  |
| dulwich_log             | 37.1 ms                                                | 29.6 ms: 1.25x faster                                                 |
| fannkuch                | 317 ms                                                 | 254 ms: 1.25x faster                                                  |
| 2to3                    | 202 ms                                                 | 163 ms: 1.25x faster                                                  |
| deepcopy_reduce         | 2.38 us                                                | 1.92 us: 1.24x faster                                                 |
| scimark_sparse_mat_mult | 3.47 ms                                                | 2.81 ms: 1.24x faster                                                 |
| async_tree_cpu_io_mixed | 670 ms                                                 | 546 ms: 1.23x faster                                                  |
| docutils                | 1.78 sec                                               | 1.45 sec: 1.23x faster                                                |
| sqlglot_optimize        | 38.0 ms                                                | 31.3 ms: 1.22x faster                                                 |
| genshi_text             | 18.4 ms                                                | 15.2 ms: 1.21x faster                                                 |
| scimark_fft             | 232 ms                                                 | 195 ms: 1.19x faster                                                  |
| bench_thread_pool       | 548 us                                                 | 462 us: 1.19x faster                                                  |
| unpack_sequence         | 38.7 ns                                                | 32.7 ns: 1.18x faster                                                 |
| sympy_integrate         | 13.4 ms                                                | 11.4 ms: 1.17x faster                                                 |
| mypy2                   | 308 ms                                                 | 263 ms: 1.17x faster                                                  |
| async_generators        | 233 ms                                                 | 200 ms: 1.16x faster                                                  |
| sqlglot_normalize       | 197 ms                                                 | 172 ms: 1.14x faster                                                  |
| dask                    | 258 ms                                                 | 226 ms: 1.14x faster                                                  |
| sympy_expand            | 276 ms                                                 | 242 ms: 1.14x faster                                                  |
| nqueens                 | 68.1 ms                                                | 60.5 ms: 1.12x faster                                                 |
| sympy_str               | 169 ms                                                 | 151 ms: 1.12x faster                                                  |
| xml_etree_generate      | 54.3 ms                                                | 48.6 ms: 1.12x faster                                                 |
| regex_v8                | 17.5 ms                                                | 15.7 ms: 1.12x faster                                                 |
| json                    | 3.10 ms                                                | 2.78 ms: 1.11x faster                                                 |
| xml_etree_parse         | 107 ms                                                 | 96.5 ms: 1.11x faster                                                 |
| sympy_sum               | 94.3 ms                                                | 85.9 ms: 1.10x faster                                                 |
| sqlite_synth            | 1.47 us                                                | 1.35 us: 1.09x faster                                                 |
| telco                   | 3.68 ms                                                | 3.39 ms: 1.08x faster                                                 |
| mdp                     | 1.67 sec                                               | 1.54 sec: 1.08x faster                                                |
| coroutines              | 20.2 ms                                                | 18.7 ms: 1.08x faster                                                 |
| regex_dna               | 160 ms                                                 | 149 ms: 1.07x faster                                                  |
| meteor_contest          | 78.6 ms                                                | 75.1 ms: 1.05x faster                                                 |
| xml_etree_iterparse     | 72.6 ms                                                | 69.4 ms: 1.05x faster                                                 |
| json_loads              | 16.9 us                                                | 16.2 us: 1.04x faster                                                 |
| pathlib                 | 28.8 ms                                                | 27.8 ms: 1.04x faster                                                 |
| python_startup          | 12.6 ms                                                | 12.3 ms: 1.03x faster                                                 |
| pidigits                | 282 ms                                                 | 281 ms: 1.00x faster                                                  |
| pickle_dict             | 17.8 us                                                | 18.0 us: 1.01x slower                                                 |
| pickle                  | 7.36 us                                                | 7.44 us: 1.01x slower                                                 |
| unpickle_list           | 2.66 us                                                | 2.70 us: 1.01x slower                                                 |
| generators              | 32.9 ms                                                | 33.7 ms: 1.02x slower                                                 |
| python_startup_no_site  | 9.73 ms                                                | 10.2 ms: 1.05x slower                                                 |
| regex_effbot            | 2.45 ms                                                | 2.61 ms: 1.07x slower                                                 |
| gc_traversal            | 2.40 ms                                                | 2.56 ms: 1.07x slower                                                 |
| bench_mp_pool           | 41.0 ms                                                | 44.0 ms: 1.07x slower                                                 |
| coverage                | 40.8 ms                                                | 57.2 ms: 1.40x slower                                                 |
| Geometric mean          | (ref)                                                  | 1.22x faster                                                          |

Benchmark hidden because not significant (3): unpickle, comprehensions, pickle_list
Ignored benchmarks (11) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, tornado_http, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.21x
- 95% likely to have a speedup of 1.20x
- 99% likely to have a speedup of 1.17x
