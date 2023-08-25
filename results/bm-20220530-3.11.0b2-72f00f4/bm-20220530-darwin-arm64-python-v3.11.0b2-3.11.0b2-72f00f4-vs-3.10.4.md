
# Results vs. 3.10.4

- fork: python
- ref: v3.11.0b2
- machine: darwin-arm64
- commit hash: 72f00f4
- commit date: 2022-05-30
- overall geometric mean: 1.20x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.16x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20220530-darwin-arm64-python-v3.11.0b2-3.11.0b2-72f00f4 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 202 ms                                                 | 162 ms: 1.25x faster                                       |
| chameleon      | 5.84 ms                                                | 4.60 ms: 1.27x faster                                      |
| docutils       | 1.78 sec                                               | 1.46 sec: 1.22x faster                                     |
| html5lib       | 44.1 ms                                                | 36.0 ms: 1.22x faster                                      |
| tornado_http   | 91.9 ms                                                | 70.8 ms: 1.30x faster                                      |
| Geometric mean | (ref)                                                  | 1.25x faster                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20220530-darwin-arm64-python-v3.11.0b2-3.11.0b2-72f00f4 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| nbody          | 94.1 ms                                                | 63.7 ms: 1.48x faster                                      |
| float          | 72.3 ms                                                | 55.2 ms: 1.31x faster                                      |
| pidigits       | 282 ms                                                 | 281 ms: 1.00x faster                                       |
| Geometric mean | (ref)                                                  | 1.25x faster                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20220530-darwin-arm64-python-v3.11.0b2-3.11.0b2-72f00f4 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 96.6 ms                                                | 77.9 ms: 1.24x faster                                      |
| regex_v8       | 17.5 ms                                                | 16.1 ms: 1.09x faster                                      |
| regex_dna      | 160 ms                                                 | 150 ms: 1.07x faster                                       |
| regex_effbot   | 2.45 ms                                                | 2.40 ms: 1.02x faster                                      |
| Geometric mean | (ref)                                                  | 1.10x faster                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20220530-darwin-arm64-python-v3.11.0b2-3.11.0b2-72f00f4 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pickle_pure_python   | 284 us                                                 | 217 us: 1.31x faster                                       |
| xml_etree_process    | 45.1 ms                                                | 34.9 ms: 1.29x faster                                      |
| unpickle_pure_python | 203 us                                                 | 176 us: 1.15x faster                                       |
| xml_etree_generate   | 54.3 ms                                                | 48.2 ms: 1.13x faster                                      |
| json_dumps           | 8.38 ms                                                | 7.63 ms: 1.10x faster                                      |
| xml_etree_iterparse  | 72.6 ms                                                | 68.8 ms: 1.06x faster                                      |
| json_loads           | 16.9 us                                                | 16.1 us: 1.05x faster                                      |
| pickle               | 7.36 us                                                | 7.06 us: 1.04x faster                                      |
| pickle_dict          | 17.8 us                                                | 17.2 us: 1.04x faster                                      |
| pickle_list          | 2.83 us                                                | 2.76 us: 1.02x faster                                      |
| xml_etree_parse      | 107 ms                                                 | 105 ms: 1.02x faster                                       |
| unpickle_list        | 2.66 us                                                | 2.70 us: 1.01x slower                                      |
| unpickle             | 9.77 us                                                | 9.98 us: 1.02x slower                                      |
| Geometric mean       | (ref)                                                  | 1.09x faster                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20220530-darwin-arm64-python-v3.11.0b2-3.11.0b2-72f00f4 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup_no_site | 9.73 ms                                                | 10.1 ms: 1.04x slower                                      |
| Geometric mean         | (ref)                                                  | 1.01x slower                                               |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20220530-darwin-arm64-python-v3.11.0b2-3.11.0b2-72f00f4 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| django_template | 27.3 ms                                                | 20.9 ms: 1.31x faster                                      |
| mako            | 10.5 ms                                                | 8.36 ms: 1.25x faster                                      |
| genshi_xml      | 37.6 ms                                                | 30.3 ms: 1.24x faster                                      |
| genshi_text     | 18.4 ms                                                | 15.2 ms: 1.21x faster                                      |
| Geometric mean  | (ref)                                                  | 1.25x faster                                               |

All benchmarks:
===============

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20220530-darwin-arm64-python-v3.11.0b2-3.11.0b2-72f00f4 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| deltablue               | 5.15 ms                                                | 2.79 ms: 1.85x faster                                      |
| logging_silent          | 119 ns                                                 | 65.3 ns: 1.82x faster                                      |
| scimark_sor             | 127 ms                                                 | 78.7 ms: 1.61x faster                                      |
| raytrace                | 328 ms                                                 | 205 ms: 1.60x faster                                       |
| go                      | 165 ms                                                 | 106 ms: 1.55x faster                                       |
| scimark_lu              | 110 ms                                                 | 71.3 ms: 1.54x faster                                      |
| richards                | 51.4 ms                                                | 33.5 ms: 1.53x faster                                      |
| crypto_pyaes            | 78.0 ms                                                | 51.5 ms: 1.51x faster                                      |
| scimark_monte_carlo     | 72.2 ms                                                | 48.7 ms: 1.48x faster                                      |
| nbody                   | 94.1 ms                                                | 63.7 ms: 1.48x faster                                      |
| pyflate                 | 453 ms                                                 | 315 ms: 1.44x faster                                       |
| async_tree_io           | 1.02 sec                                               | 711 ms: 1.43x faster                                       |
| async_tree_memoization  | 493 ms                                                 | 352 ms: 1.40x faster                                       |
| async_tree_none         | 402 ms                                                 | 291 ms: 1.38x faster                                       |
| thrift                  | 586 us                                                 | 434 us: 1.35x faster                                       |
| chaos                   | 66.8 ms                                                | 49.5 ms: 1.35x faster                                      |
| hexiom                  | 6.32 ms                                                | 4.71 ms: 1.34x faster                                      |
| spectral_norm           | 96.4 ms                                                | 72.1 ms: 1.34x faster                                      |
| logging_simple          | 4.63 us                                                | 3.48 us: 1.33x faster                                      |
| logging_format          | 5.01 us                                                | 3.76 us: 1.33x faster                                      |
| float                   | 72.3 ms                                                | 55.2 ms: 1.31x faster                                      |
| pickle_pure_python      | 284 us                                                 | 217 us: 1.31x faster                                       |
| django_template         | 27.3 ms                                                | 20.9 ms: 1.31x faster                                      |
| pycparser               | 915 ms                                                 | 702 ms: 1.30x faster                                       |
| tornado_http            | 91.9 ms                                                | 70.8 ms: 1.30x faster                                      |
| xml_etree_process       | 45.1 ms                                                | 34.9 ms: 1.29x faster                                      |
| chameleon               | 5.84 ms                                                | 4.60 ms: 1.27x faster                                      |
| mako                    | 10.5 ms                                                | 8.36 ms: 1.25x faster                                      |
| 2to3                    | 202 ms                                                 | 162 ms: 1.25x faster                                       |
| sqlalchemy_imperative   | 9.03 ms                                                | 7.25 ms: 1.25x faster                                      |
| async_tree_cpu_io_mixed | 670 ms                                                 | 539 ms: 1.24x faster                                       |
| pprint_safe_repr        | 609 ms                                                 | 490 ms: 1.24x faster                                       |
| regex_compile           | 96.6 ms                                                | 77.9 ms: 1.24x faster                                      |
| mypy2                   | 308 ms                                                 | 249 ms: 1.24x faster                                       |
| genshi_xml              | 37.6 ms                                                | 30.3 ms: 1.24x faster                                      |
| pprint_pformat          | 1.24 sec                                               | 1.01 sec: 1.23x faster                                     |
| html5lib                | 44.1 ms                                                | 36.0 ms: 1.22x faster                                      |
| docutils                | 1.78 sec                                               | 1.46 sec: 1.22x faster                                     |
| fannkuch                | 317 ms                                                 | 260 ms: 1.22x faster                                       |
| dulwich_log             | 37.1 ms                                                | 30.4 ms: 1.22x faster                                      |
| sqlalchemy_declarative  | 74.8 ms                                                | 61.9 ms: 1.21x faster                                      |
| genshi_text             | 18.4 ms                                                | 15.2 ms: 1.21x faster                                      |
| aiohttp                 | 1.29 ms                                                | 1.07 ms: 1.21x faster                                      |
| create_gc_cycles        | 876 us                                                 | 730 us: 1.20x faster                                       |
| deepcopy_memo           | 34.5 us                                                | 28.8 us: 1.20x faster                                      |
| unpack_sequence         | 38.7 ns                                                | 32.4 ns: 1.19x faster                                      |
| generators              | 32.9 ms                                                | 27.7 ms: 1.19x faster                                      |
| sqlglot_optimize        | 38.0 ms                                                | 32.0 ms: 1.19x faster                                      |
| gunicorn                | 1.34 ms                                                | 1.14 ms: 1.18x faster                                      |
| async_generators        | 233 ms                                                 | 199 ms: 1.17x faster                                       |
| bench_thread_pool       | 548 us                                                 | 468 us: 1.17x faster                                       |
| coroutines              | 20.2 ms                                                | 17.3 ms: 1.17x faster                                      |
| deepcopy                | 278 us                                                 | 238 us: 1.17x faster                                       |
| nqueens                 | 68.1 ms                                                | 58.5 ms: 1.16x faster                                      |
| scimark_fft             | 232 ms                                                 | 200 ms: 1.16x faster                                       |
| deepcopy_reduce         | 2.38 us                                                | 2.06 us: 1.16x faster                                      |
| unpickle_pure_python    | 203 us                                                 | 176 us: 1.15x faster                                       |
| sympy_integrate         | 13.4 ms                                                | 11.6 ms: 1.15x faster                                      |
| sqlglot_normalize       | 197 ms                                                 | 172 ms: 1.14x faster                                       |
| sympy_sum               | 94.3 ms                                                | 82.7 ms: 1.14x faster                                      |
| pylint                  | 307 ms                                                 | 270 ms: 1.14x faster                                       |
| dask                    | 258 ms                                                 | 227 ms: 1.14x faster                                       |
| sympy_expand            | 276 ms                                                 | 244 ms: 1.13x faster                                       |
| sympy_str               | 169 ms                                                 | 150 ms: 1.13x faster                                       |
| xml_etree_generate      | 54.3 ms                                                | 48.2 ms: 1.13x faster                                      |
| sqlglot_transpile       | 1.54 ms                                                | 1.37 ms: 1.12x faster                                      |
| sqlglot_parse           | 1.33 ms                                                | 1.19 ms: 1.12x faster                                      |
| sqlite_synth            | 1.47 us                                                | 1.34 us: 1.10x faster                                      |
| json_dumps              | 8.38 ms                                                | 7.63 ms: 1.10x faster                                      |
| json                    | 3.10 ms                                                | 2.83 ms: 1.10x faster                                      |
| regex_v8                | 17.5 ms                                                | 16.1 ms: 1.09x faster                                      |
| scimark_sparse_mat_mult | 3.47 ms                                                | 3.19 ms: 1.09x faster                                      |
| mdp                     | 1.67 sec                                               | 1.54 sec: 1.09x faster                                     |
| telco                   | 3.68 ms                                                | 3.42 ms: 1.08x faster                                      |
| regex_dna               | 160 ms                                                 | 150 ms: 1.07x faster                                       |
| xml_etree_iterparse     | 72.6 ms                                                | 68.8 ms: 1.06x faster                                      |
| pathlib                 | 28.8 ms                                                | 27.4 ms: 1.05x faster                                      |
| json_loads              | 16.9 us                                                | 16.1 us: 1.05x faster                                      |
| pickle                  | 7.36 us                                                | 7.06 us: 1.04x faster                                      |
| pickle_dict             | 17.8 us                                                | 17.2 us: 1.04x faster                                      |
| asyncio_tcp             | 673 ms                                                 | 653 ms: 1.03x faster                                       |
| pickle_list             | 2.83 us                                                | 2.76 us: 1.02x faster                                      |
| xml_etree_parse         | 107 ms                                                 | 105 ms: 1.02x faster                                       |
| regex_effbot            | 2.45 ms                                                | 2.40 ms: 1.02x faster                                      |
| meteor_contest          | 78.6 ms                                                | 77.4 ms: 1.02x faster                                      |
| pidigits                | 282 ms                                                 | 281 ms: 1.00x faster                                       |
| gc_traversal            | 2.40 ms                                                | 2.41 ms: 1.01x slower                                      |
| unpickle_list           | 2.66 us                                                | 2.70 us: 1.01x slower                                      |
| unpickle                | 9.77 us                                                | 9.98 us: 1.02x slower                                      |
| python_startup_no_site  | 9.73 ms                                                | 10.1 ms: 1.04x slower                                      |
| comprehensions          | 17.7 us                                                | 18.3 us: 1.04x slower                                      |
| bench_mp_pool           | 41.0 ms                                                | 43.7 ms: 1.07x slower                                      |
| Geometric mean          | (ref)                                                  | 1.20x faster                                               |

Benchmark hidden because not significant (1): python_startup
Ignored benchmarks (6) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, coverage, flaskblogging, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.19x
- 95% likely to have a speedup of 1.18x
- 99% likely to have a speedup of 1.16x
