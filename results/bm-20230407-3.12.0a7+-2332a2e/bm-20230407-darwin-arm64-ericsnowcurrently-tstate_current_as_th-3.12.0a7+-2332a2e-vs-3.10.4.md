
# Results vs. 3.10.4

- fork: ericsnowcurrently
- ref: tstate_current_as_th
- machine: darwin-arm64
- commit hash: 2332a2e
- commit date: 2023-04-07
- overall geometric mean: 1.17x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230407-darwin-arm64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-2332a2e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 173 ms: 1.16x faster                                                              |
| chameleon      | 5.79 ms                                                | 4.69 ms: 1.23x faster                                                             |
| docutils       | 1.78 sec                                               | 1.54 sec: 1.15x faster                                                            |
| html5lib       | 44.2 ms                                                | 37.7 ms: 1.17x faster                                                             |
| tornado_http   | 91.5 ms                                                | 70.8 ms: 1.29x faster                                                             |
| Geometric mean | (ref)                                                  | 1.20x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230407-darwin-arm64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-2332a2e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| nbody          | 93.3 ms                                                | 65.6 ms: 1.42x faster                                                             |
| float          | 72.4 ms                                                | 56.2 ms: 1.29x faster                                                             |
| pidigits       | 282 ms                                                 | 280 ms: 1.01x faster                                                              |
| Geometric mean | (ref)                                                  | 1.23x faster                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230407-darwin-arm64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-2332a2e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_compile  | 96.4 ms                                                | 78.5 ms: 1.23x faster                                                             |
| regex_v8       | 17.6 ms                                                | 16.2 ms: 1.08x faster                                                             |
| regex_dna      | 162 ms                                                 | 152 ms: 1.06x faster                                                              |
| regex_effbot   | 2.46 ms                                                | 2.65 ms: 1.08x slower                                                             |
| Geometric mean | (ref)                                                  | 1.07x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230407-darwin-arm64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-2332a2e |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| pickle_pure_python   | 283 us                                                 | 192 us: 1.47x faster                                                              |
| unpickle_pure_python | 203 us                                                 | 148 us: 1.37x faster                                                              |
| json_dumps           | 8.40 ms                                                | 6.39 ms: 1.31x faster                                                             |
| xml_etree_process    | 44.8 ms                                                | 38.5 ms: 1.16x faster                                                             |
| unpickle             | 9.89 us                                                | 9.27 us: 1.07x faster                                                             |
| json_loads           | 16.9 us                                                | 16.4 us: 1.03x faster                                                             |
| xml_etree_parse      | 106 ms                                                 | 105 ms: 1.01x faster                                                              |
| xml_etree_iterparse  | 72.3 ms                                                | 73.4 ms: 1.02x slower                                                             |
| xml_etree_generate   | 54.2 ms                                                | 56.2 ms: 1.04x slower                                                             |
| pickle               | 7.35 us                                                | 7.65 us: 1.04x slower                                                             |
| pickle_dict          | 17.9 us                                                | 18.7 us: 1.05x slower                                                             |
| unpickle_list        | 2.69 us                                                | 2.90 us: 1.08x slower                                                             |
| pickle_list          | 2.80 us                                                | 3.12 us: 1.11x slower                                                             |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230407-darwin-arm64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-2332a2e |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 11.9 ms                                                | 11.9 ms: 1.00x faster                                                             |
| python_startup_no_site | 8.88 ms                                                | 9.92 ms: 1.12x slower                                                             |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230407-darwin-arm64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-2332a2e |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mako            | 10.5 ms                                                | 7.34 ms: 1.43x faster                                                             |
| genshi_text     | 18.4 ms                                                | 14.7 ms: 1.25x faster                                                             |
| genshi_xml      | 37.2 ms                                                | 30.3 ms: 1.23x faster                                                             |
| django_template | 27.3 ms                                                | 22.6 ms: 1.21x faster                                                             |
| Geometric mean  | (ref)                                                  | 1.27x faster                                                                      |

All benchmarks:
===============

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230407-darwin-arm64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-2332a2e |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| deltablue               | 5.14 ms                                                | 2.62 ms: 1.96x faster                                                             |
| logging_silent          | 119 ns                                                 | 67.8 ns: 1.76x faster                                                             |
| richards                | 51.4 ms                                                | 30.8 ms: 1.67x faster                                                             |
| sqlglot_parse           | 1.37 ms                                                | 905 us: 1.51x faster                                                              |
| asyncio_tcp             | 670 ms                                                 | 448 ms: 1.49x faster                                                              |
| scimark_lu              | 109 ms                                                 | 73.3 ms: 1.49x faster                                                             |
| pickle_pure_python      | 283 us                                                 | 192 us: 1.47x faster                                                              |
| sqlglot_transpile       | 1.57 ms                                                | 1.08 ms: 1.46x faster                                                             |
| go                      | 165 ms                                                 | 115 ms: 1.44x faster                                                              |
| crypto_pyaes            | 78.1 ms                                                | 54.7 ms: 1.43x faster                                                             |
| async_tree_memoization  | 490 ms                                                 | 343 ms: 1.43x faster                                                              |
| mako                    | 10.5 ms                                                | 7.34 ms: 1.43x faster                                                             |
| nbody                   | 93.3 ms                                                | 65.6 ms: 1.42x faster                                                             |
| hexiom                  | 6.32 ms                                                | 4.47 ms: 1.41x faster                                                             |
| scimark_sor             | 126 ms                                                 | 90.0 ms: 1.40x faster                                                             |
| scimark_monte_carlo     | 72.5 ms                                                | 52.2 ms: 1.39x faster                                                             |
| unpickle_pure_python    | 203 us                                                 | 148 us: 1.37x faster                                                              |
| async_tree_none         | 400 ms                                                 | 295 ms: 1.36x faster                                                              |
| async_tree_io           | 1.02 sec                                               | 752 ms: 1.36x faster                                                              |
| raytrace                | 325 ms                                                 | 240 ms: 1.35x faster                                                              |
| chaos                   | 66.7 ms                                                | 49.3 ms: 1.35x faster                                                             |
| deepcopy_memo           | 34.4 us                                                | 25.8 us: 1.33x faster                                                             |
| pyflate                 | 453 ms                                                 | 341 ms: 1.33x faster                                                              |
| pycparser               | 916 ms                                                 | 695 ms: 1.32x faster                                                              |
| json_dumps              | 8.40 ms                                                | 6.39 ms: 1.31x faster                                                             |
| spectral_norm           | 95.8 ms                                                | 73.3 ms: 1.31x faster                                                             |
| tornado_http            | 91.5 ms                                                | 70.8 ms: 1.29x faster                                                             |
| float                   | 72.4 ms                                                | 56.2 ms: 1.29x faster                                                             |
| generators              | 32.7 ms                                                | 26.2 ms: 1.25x faster                                                             |
| genshi_text             | 18.4 ms                                                | 14.7 ms: 1.25x faster                                                             |
| create_gc_cycles        | 880 us                                                 | 707 us: 1.24x faster                                                              |
| chameleon               | 5.79 ms                                                | 4.69 ms: 1.23x faster                                                             |
| regex_compile           | 96.4 ms                                                | 78.5 ms: 1.23x faster                                                             |
| genshi_xml              | 37.2 ms                                                | 30.3 ms: 1.23x faster                                                             |
| pprint_pformat          | 1.23 sec                                               | 1.01 sec: 1.22x faster                                                            |
| async_tree_cpu_io_mixed | 669 ms                                                 | 548 ms: 1.22x faster                                                              |
| logging_simple          | 4.63 us                                                | 3.79 us: 1.22x faster                                                             |
| deepcopy                | 281 us                                                 | 231 us: 1.22x faster                                                              |
| pprint_safe_repr        | 606 ms                                                 | 497 ms: 1.22x faster                                                              |
| logging_format          | 4.97 us                                                | 4.11 us: 1.21x faster                                                             |
| django_template         | 27.3 ms                                                | 22.6 ms: 1.21x faster                                                             |
| dulwich_log             | 37.1 ms                                                | 30.9 ms: 1.20x faster                                                             |
| sqlalchemy_imperative   | 8.89 ms                                                | 7.48 ms: 1.19x faster                                                             |
| scimark_fft             | 230 ms                                                 | 194 ms: 1.18x faster                                                              |
| html5lib                | 44.2 ms                                                | 37.7 ms: 1.17x faster                                                             |
| scimark_sparse_mat_mult | 3.46 ms                                                | 2.95 ms: 1.17x faster                                                             |
| xml_etree_process       | 44.8 ms                                                | 38.5 ms: 1.16x faster                                                             |
| 2to3                    | 201 ms                                                 | 173 ms: 1.16x faster                                                              |
| thrift                  | 580 us                                                 | 501 us: 1.16x faster                                                              |
| deepcopy_reduce         | 2.37 us                                                | 2.05 us: 1.16x faster                                                             |
| docutils                | 1.78 sec                                               | 1.54 sec: 1.15x faster                                                            |
| mypy2                   | 307 ms                                                 | 271 ms: 1.13x faster                                                              |
| sqlglot_optimize        | 38.0 ms                                                | 33.7 ms: 1.13x faster                                                             |
| fannkuch                | 317 ms                                                 | 284 ms: 1.12x faster                                                              |
| sqlalchemy_declarative  | 74.9 ms                                                | 67.5 ms: 1.11x faster                                                             |
| unpack_sequence         | 37.4 ns                                                | 33.8 ns: 1.11x faster                                                             |
| bench_thread_pool       | 546 us                                                 | 497 us: 1.10x faster                                                              |
| sympy_integrate         | 13.3 ms                                                | 12.2 ms: 1.09x faster                                                             |
| json                    | 3.08 ms                                                | 2.83 ms: 1.09x faster                                                             |
| regex_v8                | 17.6 ms                                                | 16.2 ms: 1.08x faster                                                             |
| unpickle                | 9.89 us                                                | 9.27 us: 1.07x faster                                                             |
| regex_dna               | 162 ms                                                 | 152 ms: 1.06x faster                                                              |
| mdp                     | 1.66 sec                                               | 1.56 sec: 1.06x faster                                                            |
| sqlglot_normalize       | 196 ms                                                 | 185 ms: 1.06x faster                                                              |
| coroutines              | 20.2 ms                                                | 19.1 ms: 1.06x faster                                                             |
| meteor_contest          | 78.1 ms                                                | 74.0 ms: 1.06x faster                                                             |
| comprehensions          | 17.6 us                                                | 16.8 us: 1.05x faster                                                             |
| nqueens                 | 68.2 ms                                                | 65.7 ms: 1.04x faster                                                             |
| sympy_expand            | 275 ms                                                 | 267 ms: 1.03x faster                                                              |
| json_loads              | 16.9 us                                                | 16.4 us: 1.03x faster                                                             |
| pathlib                 | 28.8 ms                                                | 28.1 ms: 1.03x faster                                                             |
| sympy_str               | 169 ms                                                 | 166 ms: 1.02x faster                                                              |
| xml_etree_parse         | 106 ms                                                 | 105 ms: 1.01x faster                                                              |
| pidigits                | 282 ms                                                 | 280 ms: 1.01x faster                                                              |
| python_startup          | 11.9 ms                                                | 11.9 ms: 1.00x faster                                                             |
| telco                   | 3.63 ms                                                | 3.68 ms: 1.01x slower                                                             |
| xml_etree_iterparse     | 72.3 ms                                                | 73.4 ms: 1.02x slower                                                             |
| xml_etree_generate      | 54.2 ms                                                | 56.2 ms: 1.04x slower                                                             |
| pickle                  | 7.35 us                                                | 7.65 us: 1.04x slower                                                             |
| sqlite_synth            | 1.47 us                                                | 1.54 us: 1.05x slower                                                             |
| pickle_dict             | 17.9 us                                                | 18.7 us: 1.05x slower                                                             |
| regex_effbot            | 2.46 ms                                                | 2.65 ms: 1.08x slower                                                             |
| gc_traversal            | 2.39 ms                                                | 2.59 ms: 1.08x slower                                                             |
| unpickle_list           | 2.69 us                                                | 2.90 us: 1.08x slower                                                             |
| pickle_list             | 2.80 us                                                | 3.12 us: 1.11x slower                                                             |
| python_startup_no_site  | 8.88 ms                                                | 9.92 ms: 1.12x slower                                                             |
| bench_mp_pool           | 39.7 ms                                                | 46.8 ms: 1.18x slower                                                             |
| dask                    | 265 ms                                                 | 330 ms: 1.24x slower                                                              |
| async_generators        | 234 ms                                                 | 301 ms: 1.29x slower                                                              |
| coverage                | 42.0 ms                                                | 58.8 ms: 1.40x slower                                                             |
| Geometric mean          | (ref)                                                  | 1.17x faster                                                                      |

Benchmark hidden because not significant (1): sympy_sum
Ignored benchmarks (4) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, flaskblogging, gunicorn, pylint
